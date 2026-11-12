import copy
import random

from card_consts import FACEDOWN, FaceCards, PlayerType, Suite, SuiteProperties
from termcolor import colored


class Card:
    rank: int
    suite: Suite
    colour: str
    face: str
    face_up: bool

    def __init__(self, rank: int, suite: Suite, face: str = "") -> None:
        self.rank = rank
        self.suite = suite
        colour = SuiteProperties[self.suite]["colour"]
        self.colour = colour
        if face == "":
            if rank in FaceCards:
                self.face = FaceCards[rank]
            else:
                self.face = str(rank)
        else:
            self.face = face
        self.face_up = True

    def __str__(self) -> str:
        output = f"{self.face}{SuiteProperties[self.suite]['symbol']}"
        if self.face_up:
            output = colored(output, self.colour)  # pyright: ignore[reportArgumentType]
        else:
            output = FACEDOWN
        return output

    def __repr__(self) -> str:
        return f"{self.face}{SuiteProperties[self.suite]['symbol']}"

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise TypeError("cannot compare cards to non-cards")
        return self.rank == other.rank

    def __le__(self, other):
        if not isinstance(other, Card):
            raise TypeError("cannot compare cards to non-cards")
        return self.rank <= other.rank

    def __lt__(self, other):
        if not isinstance(other, Card):
            raise TypeError("cannot compare cards to non-cards")
        return self.rank < other.rank

    def __ge__(self, other):
        if not isinstance(other, Card):
            raise TypeError("cannot compare cards to non-cards")
        return self.rank >= other.rank

    def __gt__(self, other):
        if not isinstance(other, Card):
            raise TypeError("cannot compare cards to non-cards")
        return self.rank > other.rank

    def get_suite(self):
        return self.suite.value

    def get_value(self):
        return self.rank

    def flip(self):
        self.face_up = not self.face_up

    def exact_match(self, other):
        if not isinstance(other, Card):
            raise TypeError("cannot compare cards to non-cards")
        return (
            self == other
            and other.face == self.face
            and other.get_suite() == self.get_suite()
        )

    def find_in_deck(self, deck, exact=False) -> int:
        counter = 0
        for c in deck:
            if (not exact and c == self) or (self.exact_match(c)):
                counter += 1
        return counter


class Deck(list):
    def __init__(self, iterable=None):
        if iterable == None:
            iterable = []
        super().__init__(self._validate_card(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, self._validate_card(item))

    def __str__(self):
        if len(self) <=0:
            return "empty"
        return ", ".join(map(str, self))

    def peek(self, amount=1):
        temp_deck = copy.deepcopy(Deck(self[0:amount]))
        temp_deck.face_up()
        return str(temp_deck)

    def insert(self, index, item):
        super().insert(index, self._validate_card(item))

    def append(self, item):
        super().append(self._validate_card(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(self._validate_card(item) for item in other)

    def _validate_card(self, value):
        if isinstance(value, Card):
            return value
        raise TypeError(f"card expected, got {type(value).__name__}")

    def shuffle(self):
        random.shuffle(self)

    def pull_random(self) -> int:
        return random.randrange(0,len(self))

    def face_down(self):
        for i in range(len(self)):
            self[i].face_up = False

    def face_up(self):
        for i in range(len(self)):
            self[i].face_up = True

    def flip(self):
        for i in range(len(self)):
            self[i].flip()

    def sort_rank(self) -> "Deck":
        return Deck(sorted(self))

    def sort_rank_suite(self) -> "Deck":
        temp = self.copy()
        temp.sort(key=(lambda x: x.get_suite()))  # Then suite
        temp = sorted(temp)  # Sort by rank
        return Deck(temp)

    def sort_suite_rank(self) -> "Deck":
        temp = sorted(self)  # Sort by rank
        temp.sort(key=(lambda x: x.get_suite()))  # Then suite
        return Deck(temp)

    def deal(self, other, count=1):
        if count > len(self):
            raise ValueError(f"cannot deal {count} cards from a {len(self)} card deck")
        if isinstance(other, type(self)):
            target = other
        elif isinstance(other.hand, type(self)):
            target = other.hand
        else:
            raise TypeError("can only deal to a player or another deck!")
        while count > 0:
            target.insert(0, self.pop(0))
            count -= 1


class Player:
    hand: Deck
    name: str
    score: int
    type: PlayerType

    def __init__(self, name: str, type = PlayerType.HUMAN) -> None:
        self.name = name
        self.score = 0
        self.hand = Deck()
        self.type = type

    def __str__(self) -> str:
        return f"Name: {self.name} Score: {self.score} Hand: {self.hand}"

    def get_card_count(self) -> int:
        return len(self.hand)

    def sort_hand(self):
        self.hand = self.hand.sort_rank_suite()

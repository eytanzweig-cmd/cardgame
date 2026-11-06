from card_consts import FACEDOWN, FaceCards, Suite, SuiteProperties
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
        return self == other and other.face == self.face and other.get_suite() == self.get_suite()

    def find_in_deck(self, deck, exact = False) -> int:
        counter = 0
        for c in deck:
            if (not exact and c == self) or (self.exact_match(c)):
                counter += 1
        return counter

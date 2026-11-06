import copy
import random

from card_consts import Suite
from cards import Card


class Deck(list):
    def __init__(self, iterable=None):
        if iterable == None:
            iterable = []
        super().__init__(self._validate_card(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, self._validate_card(item))

    def __str__(self):
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
        if isinstance (other, type(self)):
            target = other
        elif isinstance (other.hand, type(self)):
            target = other.hand
        else :
            raise TypeError("can only deal to a player or another deck!")
        while count > 0:
            target.insert(0, self.pop(0))
            count -= 1


def full_standard_deck() -> Deck:
    new_deck = Deck()

    for i in range(4):
        for j in range(13):
            new_deck.append(Card(j + 1, Suite(i)))

    return new_deck

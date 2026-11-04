import random

from cards import Card, Suite


class Deck(list):
    def __init__(self, iterable):
        super().__init__(self._validate_card(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, self._validate_card(item))

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

    def sort_rank(self):
        return Deck(sorted(self))

    def sort_suite_rank(self):
        temp = sorted(self) #Sort by rank
        temp.sort(key=(lambda x:x.get_suite())) #Then suite
        return temp

def full_deck() -> Deck:
    new_deck = Deck([])

    for i in range(4):
        for j in range(13):
            new_deck.append(Card(j+1,Suite(i)))

    return new_deck

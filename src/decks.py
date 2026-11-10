from card_consts import Suite
from cardgame_types import Card, Deck


def full_standard_deck() -> Deck:
    new_deck = Deck()

    for i in range(4):
        for j in range(13):
            new_deck.append(Card(j + 1, Suite(i)))

    return new_deck

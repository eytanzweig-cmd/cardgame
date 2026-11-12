from card_consts import Suite
from types_cardgame import Card, Deck


def select_card(deck: Deck, idx: int) -> Card:
    return deck.pop(idx)

def full_standard_deck() -> Deck:
    new_deck = Deck()

    for i in range(4):
        for j in range(13):
            new_deck.append(Card(j + 1, Suite(i)))

    return new_deck

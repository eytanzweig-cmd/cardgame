from card_consts import MAX_VALUE, Suite
from types_cardgame import Card, Deck


# Pull a card out of a deck by index.
# Just an alias for deck.pop really
def select_card(deck: Deck, idx: int) -> Card:
    return deck.pop(idx)


# Fully populate a deck, assuming one of each card
def full_standard_deck() -> Deck:
    new_deck = Deck()

    for i in range(len(Suite)):
        for j in range(MAX_VALUE):
            new_deck.append(Card(j + 1, Suite(i)))

    return new_deck

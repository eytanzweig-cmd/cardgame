from card_consts import Suite
from cards import Card
from decks import Deck, full_deck


def main():
    card_deck = Deck([Card(10, Suite(0)), Card(12, Suite.SPADE), Card(1, Suite.DIAMOND), Card(2, Suite.HEART), Card(11, Suite.DIAMOND), Card(8, Suite.SPADE)])
    fulldeck = full_deck()

    print(f"{fulldeck}")


if __name__ == "__main__":
    main()

from card_consts import Suite
from cards import Card


def main():
    card_deck = [Card(1, Suite.CLUB, "A"), Card(2, Suite.HEART), Card(11, Suite.DIAMOND, "J")]

    print(f"{card_deck}")

    for card in card_deck:
        print(f"{card}")


if __name__ == "__main__":
    main()

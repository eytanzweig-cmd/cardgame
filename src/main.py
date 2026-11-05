from cards import Card, Suite
from decks import Deck


def main():
    aceofclubs = Card(1,Suite.CLUB)
    oneofclubs = Card(1,Suite.CLUB, "1")
    aceofspades = Card(1,Suite.SPADE)
    acedeck = Deck([aceofclubs, oneofclubs, aceofclubs, aceofspades])
    print(acedeck)
    print(aceofclubs.find_in_deck(acedeck))
    print(aceofclubs.find_in_deck(acedeck, True))

if __name__ == "__main__":
    main()

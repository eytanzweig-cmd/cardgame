from decks import full_deck, Deck


def main():
    fulldeck = full_deck()
    emptydeck = Deck([])
    fulldeck.deal(emptydeck,3)
    emptydeck.shuffle()
    print(fulldeck, emptydeck)
    emptydeck.deal(fulldeck,2)
    print(fulldeck, emptydeck)


if __name__ == "__main__":
    main()

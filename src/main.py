from decks import full_standard_deck
from players import Player


def main():
    player1 = Player("P1")
    player2 = Player("P2")
    newdeck = full_standard_deck()
    newdeck.shuffle()
    newdeck.deal(player1, 10)
    newdeck.deal(player2, 10)

    print(player1)
    print(player2)




if __name__ == "__main__":
    main()

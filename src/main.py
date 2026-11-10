from cardgame_types import Player
from decks import full_standard_deck
from ui_basic import hand_menu


def main():
    player1 = Player("P1")
    player2 = Player("P2")
    newdeck = full_standard_deck()
    newdeck.shuffle()
    newdeck.deal(player1, 10)
    newdeck.deal(player2, 10)
    i = hand_menu(player1)
    print(player1.hand[i])
    print(player2)


if __name__ == "__main__":
    main()

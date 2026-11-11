from card_consts import PlayerType
from decks import full_standard_deck
from types_cardgame import Card, Deck, Player
from ui_basic import hand_menu


def select_card(deck: Deck, idx: int) -> Card:
    return deck.pop(idx)

def make_move(player: Player):
    if player.type == PlayerType.HUMAN:
        i = hand_menu(player)
    else:
        i = player.hand.pull_random()
    card = select_card(player.hand, i)
    return card



def main():
    player1 = Player("P1", PlayerType.HUMAN)
    player2 = Player("P2", PlayerType.RANDOM)
    newdeck = full_standard_deck()
    newdeck.shuffle()
    newdeck.deal(player1, 10)
    newdeck.deal(player2, 10)
    print(player2)
    while (player2.get_card_count() > 0):
        print(make_move(player2))
    print(player2)

if __name__ == "__main__":
    main()

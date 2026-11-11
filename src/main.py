from card_consts import PlayerType
from decks import full_standard_deck
from types_cardgame import Card, Deck, Player
from ui_basic import hand_menu


def select_card(deck: Deck, idx: int) -> Card:
    return deck.pop(idx)

def make_move(player: Player):
    match player.type:
        case PlayerType.HUMAN:
            idx = hand_menu(player)
        case PlayerType.RANDOM:
            idx = player.hand.pull_random()
        case PlayerType.HIGHEST:
            idx = player.hand.index(max(player.hand))
        case PlayerType.LOWEST:
            idx = player.hand.index(min(player.hand))
        case _:
            raise ValueError("Unknown player type!")

    card = select_card(player.hand, idx)
    return card

def main():
    player1 = Player("P1 (h)", PlayerType.HIGHEST)
    player2 = Player("P2 (l)", PlayerType.LOWEST)
    newdeck = full_standard_deck()
    newdeck.shuffle()
    newdeck.deal(player1, 12)
    newdeck.deal(player2, 12)
    print(player1)
    print(player2)
    while (player2.get_card_count() > 0 and player1.get_card_count() > 0):
        p1card = make_move(player1)
        p2card = make_move(player2)
        if (p1card > p2card):
            player1.score += 1
        if (p2card > p1card):
            player2.score += 1
        print (f"{player1.name}: {p1card} vs. {player2.name}: {p2card}")
    print(player1)
    print(player2)

if __name__ == "__main__":
    main()

from card_consts import PlayerType, TURN_AMOUNT
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

    return select_card(player.hand, idx)

def main():
    player1 = Player("P1", PlayerType.HUMAN)
    player2 = Player("P2", PlayerType.RANDOM)
    dealer_deck = full_standard_deck()
    dealer_deck.shuffle()
    dealer_deck.deal(player1, 5)
    dealer_deck.deal(player2, 5)
    print(player1)
    print(player2)
    move_count = 0
    while (move_count < TURN_AMOUNT):
        if player1.get_card_count() == 0 or player2.get_card_count() == 0 or len(dealer_deck) == 0:
            raise ValueError("Out of cards!")
        dealer_card = select_card(dealer_deck, 0)
        p1card = make_move(player1)
        if (len(dealer_deck) > 1):
            dealer_deck.deal(player1, 1)
        p2card = make_move(player2)
        if (len(dealer_deck) > 0):
            dealer_deck.deal(player2, 1)
        wintext = ""
        if (p1card > dealer_card):
            player1.score += 1
            wintext += f"{player1.name} scores! "
        if (p2card > dealer_card):
            player2.score += 1
            wintext += f"{player2.name} scores! "
        if wintext == "":
            wintext = "No points"

        move_count += 1
        print (f"{move_count}: Dealer: {dealer_card}. {player1.name}: {p1card}, {player2.name}: {p2card} - {wintext}")
    print(player1)
    print(player2)

if __name__ == "__main__":
    main()

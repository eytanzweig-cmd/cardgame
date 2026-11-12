import random

from card_consts import PlayerType
from decks import full_standard_deck, select_card
from types_cardgame import Player
from ui_basic import hand_menu, hilo_bet_menu

# Constants for hi-low vs. dealer

TURN_AMOUNT = 5


def make_move(player: Player):
    match player.type:
        case PlayerType.HUMAN:
            card = select_card(player.hand, hand_menu(player))
            bet = hilo_bet_menu()
            return card, bet
        case PlayerType.RANDOM:
            idx = player.hand.pull_random()
        case PlayerType.HIGHEST:
            idx = player.hand.index(max(player.hand))
        case PlayerType.LOWEST:
            idx = player.hand.index(min(player.hand))
        case _:
            raise ValueError("Unknown player type!")
    card = select_card(player.hand, idx)
    if card.get_value() <= 6:
        bet = False # bet low
    elif card.get_value() >= 8:
        bet = True # bet high
    else:
        bet = bool(random.getrandbits(1))

    return card, bet


def dealer_hilo(P1Type, P2Type, verbose: bool = True):
    player1 = Player("P1", P1Type)
    player2 = Player("P2", P2Type)
    dealer_deck = full_standard_deck()
    dealer_deck.shuffle()
    dealer_deck.deal(player1, 5)
    dealer_deck.deal(player2, 5)
    if verbose:
        print(player1)
        print(player2)
    move_count = 0
    while move_count < TURN_AMOUNT:
        if (
            player1.get_card_count() == 0
            or player2.get_card_count() == 0
            or len(dealer_deck) == 0
        ):
            raise ValueError("Out of cards!")
        dealer_card = select_card(dealer_deck, 0)
        (p1card, p1bet) = make_move(player1)
        if len(dealer_deck) > 1:
            dealer_deck.deal(player1, 1)
        (p2card, p2bet) = make_move(player2)
        if len(dealer_deck) > 0:
            dealer_deck.deal(player2, 1)
        wintext = ""
        if (p1bet and p1card > dealer_card) or (not p1bet and p1card < dealer_card):
            player1.score += 1
            wintext += f"{player1.name} scores! "
        if (p2bet and p2card > dealer_card) or (not p2bet and p2card < dealer_card):
            player2.score += 1
            wintext += f"{player2.name} scores! "
        if wintext == "":
            wintext = "No points"

        move_count += 1
        if verbose:
            print(
            f"{move_count}: Dealer: {dealer_card}, {player1.name}: {p1card}, bet {'high' if p1bet else 'low'}, {player2.name}: {p2card}, bet {'high' if p2bet else 'low'} - {wintext}"
        )
    print(f"{player1.name} - final score: {player1.score}")
    print(f"{player2.name} - final score: {player2.score}")

    if player1.score > player2.score:
        print(f"{player1.name} wins!")
        return 1
    elif player2.score > player1.score:
        print(f"{player2.name} wins!")
        return 2
    else:
        print("Tie!")
        return 0

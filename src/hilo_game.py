import copy
import random

from card_consts import MAX_VALUE, OutputType, PlayerType
from decks import full_standard_deck, select_card
from types_cardgame import Player
from ui_basic import hand_menu, hilo_bet_menu

# Constants for High/low game

STARTING_HAND_SIZE = 5

# Return a bet as to whether a particular chosen value is high (true) or low (false)
def set_bet_by_value(value, midpoint: float = (MAX_VALUE + 1) / 2) -> bool:
    if float(value) == midpoint:
        return bool(random.getrandbits(1))  # If we're exactly halfway, bet randomly
    else:
        return value > midpoint


# Calculate the average value of all the cards in a standard deck that the player hasn't seen
# This is inefficient, improve it
def rest_of_deck_avg(player: Player):
    rest_of_deck = full_standard_deck() - player.seen
    return rest_of_deck.get_average_value()


# Make a move based on playertype
def make_move(player: Player):
    # avg_value = full_standard_deck().get_average_value()
    match player.type:
        case PlayerType.HUMAN:
            card = select_card(player.hand, hand_menu(player))
            bet = hilo_bet_menu()
        case PlayerType.RANDOM:
            card = select_card(player.hand, player.hand.pull_random())
            bet = set_bet_by_value(card.get_value())
        case PlayerType.HIGHEST:
            card = select_card(player.hand, player.hand.index(max(player.hand)))
            bet = set_bet_by_value(card.get_value())
        case PlayerType.LOWEST:
            card = select_card(player.hand, player.hand.index(min(player.hand)))
            bet = set_bet_by_value(card.get_value())
        case PlayerType.SMART:
            avg = rest_of_deck_avg(player)
            hi = max(player.hand).rank
            lo = min(player.hand).rank
            if (hi - avg) > (avg - lo):
                pick = max(player.hand)
            else:
                pick = min(player.hand)
            card = select_card(player.hand, player.hand.index(pick))
            bet = set_bet_by_value(card.get_value(), avg)
        case _:
            raise ValueError("Unknown player type!")
    return card, bet


def dealer_hilo(
    turn_amount: int, P1Type, P2Type, output: OutputType = OutputType.NORMAL
):
    player1 = Player("P1", P1Type)
    player2 = Player("P2", P2Type)
    dealer_deck = full_standard_deck()
    dealer_deck.shuffle()
    dealer_deck.deal(player1, STARTING_HAND_SIZE)
    dealer_deck.deal(player2, STARTING_HAND_SIZE)
    if player1.type == PlayerType.HUMAN or output == OutputType.VERBOSE:
        print(player1)
    if player2.type == PlayerType.HUMAN or output == OutputType.VERBOSE:
        print(player2)
    move_count = 0
    while move_count < turn_amount:
        if len(dealer_deck) <= 2: # Dealer needs 3 cards per turn
            if output != OutputType.SILENT:
                print("Dealer low on cards, picks up discarded cards!")
            dealer_deck = full_standard_deck() # Reset dealer deck
            dealer_deck -= player1.hand # Take out the cards player 1 has
            dealer_deck -= player2.hand # Take out the cards player 2 has
            if output == OutputType.VERBOSE:
                print(dealer_deck)
            dealer_deck.shuffle()
            player1.seen = copy.deepcopy(player1.hand) # And both players should reset their memories
            player2.seen = copy.deepcopy(player2.hand)
        dealer_card = select_card(dealer_deck, 0)
        (p1card, p1bet) = make_move(player1)
        dealer_deck.deal(player1, 1)
        (p2card, p2bet) = make_move(player2)
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

        player1.seen.append(p2card)
        player2.seen.append(p1card)
        player1.seen.append(dealer_card)
        player2.seen.append(dealer_card)

        move_count += 1
        if output != OutputType.SILENT:
            print(
                f"{move_count}: Dealer: {dealer_card}, {player1.name}: {p1card}, bet {'high' if p1bet else 'low'}, {player2.name}: {p2card}, bet {'high' if p2bet else 'low'} - {wintext}"
            )
    if output != OutputType.SILENT:
        print(f"{player1.name} - final score: {player1.score}")
        print(f"{player2.name} - final score: {player2.score}")

    if player1.score > player2.score:
        if output != OutputType.SILENT:
            print(f"{player1.name} wins!")
        return 1
    elif player2.score > player1.score:
        if output != OutputType.SILENT:
            print(f"{player2.name} wins!")
        return 2
    else:
        if output != OutputType.SILENT:
            print("Tie!")
        return 0

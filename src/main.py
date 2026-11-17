from card_consts import Suite
from decks import full_standard_deck
from hilo_game import dealer_hilo, set_bet_by_value
from types_cardgame import Card, Deck, PlayerType


def run_n(n):
    win_count = {0: 0, 1: 0, 2: 0}
    for i in range(n):
        win = dealer_hilo(PlayerType.RANDOM, PlayerType.COUNTER, False)
        win_count[win] += 1
    print(win_count)


def main():
    run_n(10000)


if __name__ == "__main__":
    main()

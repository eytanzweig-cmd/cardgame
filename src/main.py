from hilo_game import dealer_hilo
from types_cardgame import PlayerType, Deck, Card
from decks import full_standard_deck
from card_consts import Suite

def run_n(n):
    win_count = {0: 0, 1: 0, 2: 0}
    for i in range(n):
        win = dealer_hilo(PlayerType.RANDOM, PlayerType.RANDOM, False)
        win_count[win] += 1
    print(win_count)


def main():
    deck1 = full_standard_deck()
    deck2 = Deck([Card(1,Suite.HEART)])
    attempt = deck1 + deck1
    print(attempt)
    run_n(10)

if __name__ == "__main__":
    main()

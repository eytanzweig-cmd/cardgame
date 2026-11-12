from hilo_game import dealer_hilo
from types_cardgame import PlayerType


def main():
    dealer_hilo(PlayerType.HUMAN, PlayerType.RANDOM, True)


if __name__ == "__main__":
    main()

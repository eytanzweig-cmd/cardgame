from types_cardgame import PlayerType
from hilo_game import dealer_hilo


def main():
    dealer_hilo(PlayerType.RANDOM, PlayerType.RANDOM, True)


if __name__ == "__main__":
    main()

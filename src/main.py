from card_consts import OutputType, PlayerType
from hilo_game import dealer_hilo


# Run the game many times and record wins/ties. Used to test computer players.
def run_n(n):
    win_count = {0: 0, 1: 0, 2: 0}
    for i in range(n):
        win = dealer_hilo(5, PlayerType.SMART, PlayerType.RANDOM, OutputType.SILENT)
        win_count[win] += 1
    print(win_count)


def main():
    dealer_hilo(5, PlayerType.HUMAN, PlayerType.SMART, OutputType.NORMAL)
    # run_n(10000)


if __name__ == "__main__":
    main()

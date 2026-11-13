from hilo_game import dealer_hilo
from types_cardgame import PlayerType

def run_n(n):
    win_count = {0:0,1:0,2:0}
    for i in range(n):
        win = dealer_hilo(PlayerType.RANDOM, PlayerType.RANDOM, False)
        win_count[win] += 1
    print(win_count)

def main():
    run_n(10000)

if __name__ == "__main__":
    main()

def print_card_sequence(deck):
    for counter, card in enumerate(deck):
        print(f"{counter+1}. {card}")



def hand_menu(player):
    if len(player.hand) == 0:
        print ("No cards to pick from!")
        return -1
    counter = len(player.hand)
    print_card_sequence(player.hand)
    valid = False
    index = 0
    while valid == False:
        response = input("Pick a card>")
        try:
            index = int(response)
        except ValueError:
            print("Invalid response!")
            continue
        if index <= 0 or index > counter:
            print("Invalid response!")
            continue
        valid = True
    return index-1


def hilo_bet_menu():
    valid = False
    response = ""
    while valid == False:
        response = input("Bet (h)igh or (l)ow>")
        if response.lower() != "h" and response.lower() != "l":
            print("Invalid response!")
            continue
        valid = True
    return response.lower() == "h"

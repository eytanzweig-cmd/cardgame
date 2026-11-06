from decks import full_standard_deck


def main():
    newdeck = full_standard_deck()
    newdeck.face_down()
    newdeck.shuffle()
    print(newdeck.peek(3))
    print(newdeck)


if __name__ == "__main__":
    main()

from cards import Card
from termcolor import colored


def main():
    testcard = Card(1, "green", "A")
    newcard = Card(2, "red")

    print(f"{testcard}, {newcard}")


if __name__ == "__main__":
    main()

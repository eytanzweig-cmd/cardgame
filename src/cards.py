from termcolor import colored
from termcolor._types import Color


class Card:
    value: int
    colour: Color
    face: str

    def __init__(self, value: int, colour: Color, face: str = "") -> None:
        self.value = value
        self.colour = colour
        if face == "":
            self.face = str(value)
        else:
            self.face = face

    def __str__(self) -> str:
        return colored(f"{self.face}", self.colour)


class Deck:
    cards: list[Card]

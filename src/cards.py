from termcolor import colored


class Card:
    value: int
    colour: str
    face: str

    def __init__(self, value:int, colour: str, face:str = "") -> None:
        self.value = value
        self.colour = colour
        if (face == ""):
            self.face = str(value)
        else:
            self.face = face

    def __str__(self) -> str:
        return colored(f"{self.face}", self.colour)

class Deck:
    cards: list[Card]

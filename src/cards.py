from card_consts import Suite, SuiteProperties
from termcolor import colored


class Card:
    rank: int
    suite: Suite
    colour: str
    face: str

    def __init__(self, rank: int, suite: Suite, face: str = "") -> None:
        self.rank = rank
        self.suite = suite
        colour = SuiteProperties[self.suite]["colour"]
        self.colour = colour
        if face == "":
            self.face = str(rank)
        else:
            self.face = face

    def __repr__(self) -> str:
        return colored(
            f"{self.face}{SuiteProperties[self.suite]['symbol']}", self.colour  # pyright: ignore[reportArgumentType]
        )

from card_consts import FaceCards, Suite, SuiteProperties
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
            if rank in FaceCards:
                self.face = FaceCards[rank]
            else:
                self.face = str(rank)
        else:
            self.face = face

    def __repr__(self) -> str:
        return colored(
            f"{self.face}{SuiteProperties[self.suite]['symbol']}",
            self.colour,  # pyright: ignore[reportArgumentType]
        )

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise TypeError("cannot compare cards to non-cards")
        return self.rank == other.rank

    def __le__(self, other):
        if not isinstance(other, Card):
            raise TypeError("cannot compare cards to non-cards")
        return self.rank <= other.rank

    def __lt__(self, other):
        if not isinstance(other, Card):
            raise TypeError("cannot compare cards to non-cards")
        return self.rank < other.rank

    def __ge__(self, other):
        if not isinstance(other, Card):
            raise TypeError("cannot compare cards to non-cards")
        return self.rank >= other.rank

    def __gt__(self, other):
        if not isinstance(other, Card):
            raise TypeError("cannot compare cards to non-cards")
        return self.rank > other.rank

    def get_suite(self):
        return self.suite.value

    def get_value(self):
        return self.rank

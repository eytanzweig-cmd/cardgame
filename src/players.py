from decks import Deck


class Player:
    hand: Deck
    name: str
    score: int

    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0
        self.hand = Deck()

    def __str__(self) -> str:
        return f"Name: {self.name} Score: {self.score} Hand: {self.hand}"

    def sort_hand(self):
        self.hand = self.hand.sort_rank_suite()

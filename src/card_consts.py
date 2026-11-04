from enum import Enum


class Suite(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3

SuiteProperties = {
    Suite.CLUB: {"colour": "black", "symbol": "\u2663"},
    Suite.SPADE: {"colour": "black", "symbol": "\u2660"},
    Suite.DIAMOND: {"colour": "red", "symbol": "\u2666"},
    Suite.HEART: {"colour": "red", "symbol": "\u2665"},
}

FaceCards = {
    1: "A",
    11: "J",
    12: "Q",
    13: "K",
}

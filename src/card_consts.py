from enum import Enum

FACEDOWN = "??"

class Suite(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3

class PlayerType(Enum):
    HUMAN = 0
    RANDOM = 1
    HIGHEST = 2
    LOWEST = 3

SuiteProperties = {
    Suite.CLUB: {"colour": "blue", "symbol": "\u2663"},
    Suite.SPADE: {"colour": "blue", "symbol": "\u2660"},
    Suite.DIAMOND: {"colour": "red", "symbol": "\u2666"},
    Suite.HEART: {"colour": "red", "symbol": "\u2665"},
}

FaceCards = {
    1: "A",
    11: "J",
    12: "Q",
    13: "K",
}

from enum import Enum

FACEDOWN = "??"
MAX_VALUE = 13

class OutputType(Enum):
    SILENT = 0   # Game won't print anything to stdout (weird if there's a human player)
    NORMAL = 1   # Game will print the expected information a human player should have to stdout
    VERBOSE = 2  # Game will print information about the game state a human player shouldn't have to stdou

class PlayerType(Enum):
    HUMAN = 0
    RANDOM = 1
    HIGHEST = 2
    LOWEST = 3
    SMART = 4

class Suite(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3

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

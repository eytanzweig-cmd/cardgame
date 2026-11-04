from enum import Enum


class Suite(Enum):
    CLUB = 0
    SPADE = 1
    DIAMOND = 2
    HEART = 3


SuiteProperties = {
    Suite.CLUB: {"colour": "black", "symbol": "\u2663"},
    Suite.SPADE: {"colour": "black", "symbol": "\u2660"},
    Suite.DIAMOND: {"colour": "red", "symbol": "\u2666"},
    Suite.HEART: {"colour": "red", "symbol": "\u2665"},
}

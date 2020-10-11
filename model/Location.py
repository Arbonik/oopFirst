from enum import Enum
from random import Random


class Location(Enum):
    HOME = 1
    WITH_RELATIONS = 2
    DIRMOTORY = 3

    @staticmethod
    def random():
        return (Location.DIRMOTORY, Location.HOME, Location.WITH_RELATIONS)[Random().randint(0,2)]
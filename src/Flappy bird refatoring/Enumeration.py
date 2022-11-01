from enum import Enum


class Sounds(Enum):
    FLAP = 1
    DEATH = 2
    SCORE = 3
class SaveData(Enum):
    HIGH_SCORE = 1
    SCORE = 2

class GameBackground(Enum):
    NIGHT = 1
    DAY =2
class BirdColor(Enum):
    BLUE = 1
    RED = 2
    YELLOW =3
class PipeColor(Enum):
    GREEN = 1
    RED = 2
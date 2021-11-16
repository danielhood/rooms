from enum import IntEnum

class CommandType(IntEnum):
    NONE = 0
    EXIT = 1
    HELP = 2
    MOVE = 3
    LOOK = 4
    LOOKAT = 5
    TAKE = 6
    DROP = 7

class Direction(IntEnum):
    N = 0
    NE = 1
    E = 2
    SE = 3
    S = 4
    SW = 5
    W = 6
    NW = 7
    U = 8
    D = 9

class Command:
    def __init__(self, commandType, direction = None, target = None):
        self.commandType = commandType
        self.direction = direction
        self.target = target

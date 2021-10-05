# -*- coding: utf-8 -*-
from enum import Enum

class Action(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def next_position(self, position):
        return (self.value[0] + position[0], self.value[1] + position[1])

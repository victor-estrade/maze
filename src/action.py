# -*- coding: utf-8 -*-
from enum import Enum

class Action(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

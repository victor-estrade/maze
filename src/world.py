# -*- coding: utf-8 -*-


import numpy as np


EMPTY = 0
WALL = 1
EXIT = 2
START = 3

CELL_TO_STR = {
    EMPTY: " ",
    WALL: "█",
    EXIT: "H",
    START: "O",
}

class MazeGenerator():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def generate(self):
        grid = np.random.randint(0, 2, size=(self.height, self.width))
        start_x = np.random.randint(self.width)
        start_y = np.random.randint(self.height)
        grid[start_y, start_x] = START
        exit_x = np.random.randint(self.width)
        exit_y = np.random.randint(self.height)
        while exit_x == start_x and exit_y == start_y:
            exit_x = np.random.randint(self.width)
            exit_y = np.random.randint(self.height)
        grid[exit_y, exit_x] = EXIT
        return grid



class MazeEnv():
    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        top = ("#" * (self.grid.shape[1] + 2 ) ) + "\n"
        str = top
        str += "\n".join([f"#{''.join([CELL_TO_STR[cell] for cell in line])}#" for line in self.grid])
        str += "\n" + top
        return str

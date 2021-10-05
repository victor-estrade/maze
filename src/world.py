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


class DummyWorldGenerator():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rng = np.random.default_rng()

    def generate(self):
        grid = self.rng.integers(0, 2, size=(self.height, self.width))
        start_x = self.rng.integers(self.width)
        start_y = self.rng.integers(self.height)
        grid[start_y, start_x] = START
        exit_x = self.rng.integers(self.width)
        exit_y = self.rng.integers(self.height)
        while exit_x == start_x and exit_y == start_y:
            exit_x = self.rng.integers(self.width)
            exit_y = self.rng.integers(self.height)
        grid[exit_y, exit_x] = EXIT
        return grid


class WorldGenerator():
    def __init__(self, height, width, n_walls, seed=None):
        self.height = height
        self.width = width
        self.n_walls = n_walls
        self.rng = np.random.default_rng(seed)

    def random_cell(self):
        x = self.rng.integers(self.width)
        y = self.rng.integers(self.height)
        return x, y

    def neighbour(self, x, y):
        cells = []
        if x + 1 < self.width:
            cells.append((x+1, y))
        if x - 1 >= 0:
            cells.append((x-1, y))
        if y + 1 < self.height:
            cells.append((x, y+1))
        if y - 1 >= 0:
            cells.append((x, y-1))
        return cells

    def random_neighbour(self, x, y):
        cells = self.neighbour(x, y)
        i = self.rng.integers(len(cells))
        picked_cell = cells[i]
        return picked_cell

    def generate(self):
        grid = np.ones((self.height, self.width))
        current_x, current_y = self.random_cell()
        grid[current_y, current_x] = EMPTY
        while grid.sum() >= self.n_walls:
            current_x, current_y = self.random_neighbour(current_x, current_y)
            grid[current_y, current_x] = EMPTY

        start_x, start_y = self.random_cell()
        while grid[start_y, start_x] != EMPTY:
            start_x, start_y = self.random_cell()
        grid[start_y, start_x] = START

        exit_x, exit_y = self.random_cell()
        while grid[exit_y, exit_x] != EMPTY:
            exit_x, exit_y = self.random_cell()
        grid[exit_y, exit_x] = EXIT

        return grid, (start_x, start_y), (exit_x, exit_y)



class WorldGeneratorBetter(WorldGenerator):

    def generate(self):
        grid = np.ones((self.height, self.width))
        x, y = self.random_cell()
        grid[y, x] = EMPTY
        dig_candidates = self.neighbour(x, y)
        while grid.sum() >= self.n_walls:
            idx = self.rng.integers(len(dig_candidates))
            x, y = dig_candidates[idx]
            grid[y, x] = EMPTY
            cells = self.neighbour(x, y)
            cells = [c for c in cells if grid[c[1], c[0]] == WALL]
            dig_candidates += cells

        start_x, start_y = self.random_cell()
        while grid[start_y, start_x] != EMPTY:
            start_x, start_y = self.random_cell()
        grid[start_y, start_x] = START

        exit_x, exit_y = self.random_cell()
        while grid[exit_y, exit_x] != EMPTY:
            exit_x, exit_y = self.random_cell()
        grid[exit_y, exit_x] = EXIT

        return grid


class WorldEnv():
    def __init__(self, grid, start, exit):
        self.grid = grid
        self.start = start
        self.state = start
        self.exit = exit

    def __str__(self):
        top = ("#" * (self.grid.shape[1] + 2 ) ) + "\n"
        str = top
        str += "\n".join([f"#{''.join([CELL_TO_STR[cell] for cell in line])}#" for line in self.grid])
        str += "\n" + top
        return str

    def step(self, action, observation):
        pass

    def reset(self):
        self.state = self.start

    def render(self):
        print(self)

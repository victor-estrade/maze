# -*- coding: utf-8 -*-

import numpy as np

from src.action import Action

EMPTY = 0
WALL = 1
EXIT = 2
START = 3
PLAYER = 4

CELL_TO_STR = {
    EMPTY: " ",
    WALL: "█",
    EXIT: "H",
    START: "O",
    PLAYER: "i"
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
        self.cumulative_reward = 0

        self._reward_table = {EMPTY:0, WALL:-5, START:0, EXIT:25}

    def __str__(self):
        grid = np.array(self.grid, copy=True)
        x, y = self.state
        grid[y, x] = PLAYER

        top = ("#" * (self.grid.shape[1] + 2 ) ) + "\n"
        str = top
        str += "\n".join([f"#{''.join([CELL_TO_STR[cell] for cell in line])}#" for line in grid])
        str += "\n" + top
        return str

    def reset(self):
        self.state = self.start
        self.cumulative_reward = 0

    def render(self):
        print(self)

    def is_out_of_grid(self, x, y):
        return x < 0 or x >= self.grid.shape[1] or y < 0 or y >= self.grid.shape[0]

    def cell_at(self, x, y):
        """ Returns the cell content. If (x, y) is out of the grid the cell is assumed to be a WALL."""
        if self.is_out_of_grid(x, y):
            return WALL
        else:
            return self.grid[y, x]

    def is_reachable(self, x, y):
        return self.cell_at(x, y) != WALL

    def is_exit(self, x, y):
        return self.cell_at(x, y) == EXIT

    def step(self, action, observation):
        next_xy = np.array(self.state) + np.array(action.value)
        x, y = next_xy[0], next_xy[1]

        reward = self._reward_table[self.cell_at(x, y)]
        reward -= 1
        self.cumulative_reward += reward

        if self.is_reachable(x, y):
            self.state = (x, y)

        done = self.is_exit(x, y) or self.cumulative_reward < -200
        observation = self.state
        return observation, reward, done

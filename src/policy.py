# -*- coding: utf-8 -*-

import numpy as np

from src.pathfinder import shortest_path_grid
from src.action import Action


class ShortestPathPolicy():
    def __init__(self, world):
        self.world = world
        self.path_grid = shortest_path_grid(world, *world.exit)

    def path_value(self, x, y):
        return self.path_grid[y, x]

    def next_move(self, state):
        possible_moves = list(Action)
        min_value = np.max(self.path_grid)
        for move in possible_moves:
            next_position = move.next_position(state)
            if self.world.is_reachable(*next_position):
                value = self.path_value(*next_position)
                if value < min_value :
                    min_value = value
                    best_move = move
        print(f"state = {state} next position {move.next_position(state)}")
        return best_move

# -*- coding: utf-8 -*-

from world import EMPTY, WALL, EXIT, START


def shortest_path_grid(grid, start_x, start_y):
    longest_path = grid.size
    distance_grid = np.zeros_like(grid)

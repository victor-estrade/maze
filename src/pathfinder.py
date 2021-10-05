# -*- coding: utf-8 -*-
import numpy as np

from world import EMPTY, WALL, EXIT, START



def shortest_path_grid(world, start_x, start_y):
    longest_path = world.grid.size + 1
    distance_grid = np.zeros_like(world.grid) + longest_path
    distance_grid[start_y, start_x] = 0
    frontiere = set(world.get_reachable_neighboor(start_x, start_y))
    while frontiere :
        # print(f"the new frontiere is {frontiere}")
        x, y = frontiere.pop()
        # print(f"exploring {x,y}")
        neighbour = world.get_reachable_neighboor(x, y)
        # print(f"neighbour {neighbour}")
        distance_grid[y, x] = min([distance_grid[n_y, n_x] + 1 for n_x, n_y in neighbour])
        to_explore = [(n_x, n_y) for n_x, n_y in neighbour if distance_grid[n_y, n_x] >= longest_path]
        frontiere.update(to_explore)
        # print(f"new cell to exlore = {to_explore}")
        # print('---')
    return distance_grid

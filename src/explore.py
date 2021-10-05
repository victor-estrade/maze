# -*- coding: utf-8 -*-

import click
import logging

from src.world import WorldGenerator, WorldEnv
from src.action import Action
from src.game import Game
from src.agent import RandomAgent
from src.pathfinder import shortest_path_grid
from src.policy import ShortestPathPolicy
from src.q_function import Qfunction

import numpy as np

@click.command()
def main():
    print("Hello world")

    WIDTH = 5
    HEIGHT = 7
    N_WALLS = HEIGHT * WIDTH // 3
    SEED = None
    grid, start, exit = WorldGenerator(WIDTH, HEIGHT, N_WALLS, seed=SEED).generate()
    #
    # grid = np.array([[0., 0., 0., 1., 1., 1., 1.,],
    #                  [0., 0., 0., 0., 0., 1., 1.,],
    #                  [1., 0., 0., 0., 0., 0., 1.,],
    #                  [0., 0., 0., 0., 3., 0., 2.,],
    #                  [0., 0., 0., 1., 1., 0., 0.,]]
    #                 )
    # start = (4, 3)
    # exit = (6, 3)
    env = WorldEnv(grid, start, exit)
    print(grid)
    env.render()
    print(exit)
    res = shortest_path_grid(env, *exit)
    print(res)
    policy = ShortestPathPolicy(env)
    move = policy.next_move(start)
    print(f"move = {move}")
    q_function = Qfunction(env, policy)
    q_value = q_function.q_value(move, start)
    print(f"q-value = {q_value}")









if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()

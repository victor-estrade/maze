# -*- coding: utf-8 -*-

import click
import logging

from src.world import WorldGenerator, WorldEnv
from src.action import Action
from src.game import Game
from src.agent import PolicyDrivenAgent
from src.policy import ShortestPathPolicy
from src.q_function import TabularQfunction

import numpy as np

@click.command()
def main():
    print("Hello world")

    WIDTH = 10
    HEIGHT = 13
    N_WALLS = HEIGHT * WIDTH // 3
    SEED = 42
    grid, start, exit = WorldGenerator(WIDTH, HEIGHT, N_WALLS, seed=SEED).generate()
    env = WorldEnv(grid, start, exit)
    env.render()
    policy = ShortestPathPolicy(env)
    agent = PolicyDrivenAgent(policy)
    game = Game(env, agent)
    game.play()






if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()

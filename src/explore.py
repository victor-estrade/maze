
import click
import logging

from src.world import WorldGenerator, WorldEnv
from src.action import Action

@click.command()
def main():
    print("Hello world")

    WIDTH = 10
    HEIGHT = 13
    N_WALLS = 13*5
    SEED = 42
    grid, start, exit = WorldGenerator(WIDTH, HEIGHT, N_WALLS, seed=SEED).generate()
    env = WorldEnv(grid, start, exit)
    env.render()
    print(Action.UP)
    print(Action.UP.value)



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()

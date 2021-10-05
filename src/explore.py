
import click
import logging

from src.world import WorldGenerator, WorldEnv

@click.command()
def main():
    print("Hello world")

    WIDTH = 10
    HEIGHT = 13
    N_WALLS = 13*5
    grid = WorldGenerator(WIDTH, HEIGHT, N_WALLS).generate()
    print(grid)
    env = WorldEnv(grid)
    print(env)



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()

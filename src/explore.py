
import click
import logging

from src.world import MazeGenerator, MazeEnv

@click.command()
def main():
    print("Hello world")

    grid = MazeGenerator(5, 7).generate()
    print(grid)
    env = MazeEnv(grid)
    print(env)



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()

#!/usr/bin/env python3

"""This is where all the functions goes in the game"""

from connect_4.game import Game


def main():
    """Main function to run the game"""

    the_game = Game()
    return the_game.run()


if __name__ == '__main__':
    main()

# Main game loop, user enters y/n if they want to start a new game.

from chess.objects import Board, Game

if __name__ == '__main__':

    print('Welcome to chess!  Starting a new game.')

    game = Game()

    done = False
    while not done:
        game.start()
        done = input("Start new game? (y/n) ") != 'y'


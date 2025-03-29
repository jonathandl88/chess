# Contains objects that make up chess game.

from abc import ABC, abstractmethod

class Color:
    WHITE = 'white'
    BLACK = 'black'

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = Color.WHITE

    def start(self):
        self.setupNewGame()
        self.loop()

    def loop(self):
        winner = None
        while not winner:
            pass

    def setupNewGame(self):
        self.turn = Color.WHITE
        self.board.setupNewGame()

    def getPossibleMoves(self):
        pass


class Board:
    def __init__(self):
        self.positions = [[Position(f'{char}{num}') for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']] for num in range(1, 9)]

    def __str__(self):
        for rank in range(1, 9):
            for file in range(1, 9):
                print(str(self.positions[rank][file]), end='')
            print()

    def setupNewGame(self):
        """Sets up a new game by clearing pieces and reinitializing"""
        for pos in self.positions:
            pos.piece = None
        
        # white pieces

        for pos in self.positions[1]:
            pos.piece = Pawn(Color.WHITE)

        self.positions[0][0] = Rook(Color.WHITE)
        self.positions[0][7] = Rook(Color.WHITE)
        self.positions[0][1] = Knight(Color.WHITE)
        self.positions[0][6] = Knight(Color.WHITE)
        self.positions[0][2] = Bishop(Color.WHITE)
        self.positions[0][5] = Bishop(Color.WHITE)
        self.positions[0][3] = Queen(Color.WHITE)
        self.positions[0][4] = King(Color.WHITE)

        # black pieces

        for pos in self.positions[6]:
            pos.piece = Pawn(Color.BLACK)

        self.positions[7][0] = Rook(Color.BLACK)
        self.positions[7][7] = Rook(Color.BLACK)
        self.positions[7][1] = Knight(Color.BLACK)
        self.positions[7][6] = Knight(Color.BLACK)
        self.positions[7][2] = Bishop(Color.BLACK)
        self.positions[7][5] = Bishop(Color.BLACK)
        self.positions[7][3] = Queen(Color.BLACK)
        self.positions[7][4] = King(Color.BLACK)


class Position:
    def __init__(self, name):
        self.name = name
        self.piece = None
        

class ChessPiece(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def check_legal_moves(self):
        pass

class Pawn(ChessPiece):
    def __init__(self, color):
        self.color = color

class Rook(ChessPiece):
    pass

class Bishop(ChessPiece):
    pass

class Knight(ChessPiece):
    pass

class Queen(ChessPiece):
    pass

class King(ChessPiece):
    def has_moved(self):
        pass
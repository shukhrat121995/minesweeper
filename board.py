from piece import Piece
from random import random


class Board:
    """
    Board class that is responsible for initializing the board with given column
    and row
    """
    def __init__(self, size, probability):
        """Constructor of the Board class"""
        self.size = size
        self.probability = probability
        self.set_board()

    def set_board(self):
        """
        Create a board based on the size value
        :return:
        """
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                # random function just returns floating number between 0 and 1
                # so that your probability variable should not be below 0 and above 1
                has_bomb = random() < self.probability
                piece = Piece(has_bomb=has_bomb)
                row.append(piece)
            self.board.append(row)

    def get_size(self):
        """
        Return the size of the board
        """
        return self.size

    def get_piece(self, row, col):
        """
        Return individual piece based on the row and col values
        """
        return self.board[row][col]

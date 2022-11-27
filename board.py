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
        self.board = []
        self.lost = False
        self.number_of_clicks = 0
        self.number_of_non_bombs = 0
        self.set_board()

    def set_board(self):
        """
        Create a board based on the size value
        """
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                # random function just returns floating number between 0 and 1
                # so that your probability variable should not be below 0 and above 1
                has_bomb = random() < self.probability
                if not has_bomb:
                    self.number_of_non_bombs += 1
                piece = Piece(has_bomb=has_bomb)
                row.append(piece)
            self.board.append(row)
        self.set_neighbours()

    def set_neighbours(self):
        """
        Set neighbours of the current piece with the help of set_neighbours function
        in the Piece class
        """
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.get_piece(row, col)
                neighbours = self.get_list_of_neighbours(row, col)
                piece.set_neighbours(neighbours)

    def get_list_of_neighbours(self, row, col):
        """
        Iterate like a circle around the piece and get its neighbours
        * * *
        * X *
        * * *
        """
        neighbours = []
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                is_ouf_of_bounds = r < 0 or r >= self.size[0] or c < 0 or c >= self.size[1]
                is_same = r == row and c == col
                if is_same or is_ouf_of_bounds:
                    continue
                neighbours.append(self.get_piece(r, c))
        return neighbours

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

    def handle_click(self, piece, flag):
        """
        Check whether the piece already clicked or flagged
        """
        if piece.get_clicked() or (not flag and piece.get_flagged()):
            return
        if flag:
            piece.toggle_flag()
            return
        piece.click()
        if piece.get_has_bomb():
            self.lost = True
            return

        self.number_of_clicks += 1

        if piece.get_number_around() != 0:
            # As we are calling this function recursively we need a termination
            # condition. When there are no more bombs to explore just return
            return

        for neighbour in piece.get_neighbours():
            if not neighbour.get_has_bomb() and not neighbour.get_clicked():
                self.handle_click(neighbour, False)

    def get_lost(self):
        """
        Just return the lost state of variable
        """
        return self.lost

    def get_won(self):
        """
        Return True if the number of non bombs is equal to the
        number of user's clicks
        """
        return self.number_of_non_bombs == self.number_of_clicks




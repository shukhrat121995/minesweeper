class Piece:
    """
    Piece class that represents each individual piece
    """
    def __init__(self, has_bomb):
        """
        Constructor of the Piece class
        """
        self.has_bomb = has_bomb
        self.clicked = False
        self.flagged = False

    def get_has_bomb(self):
        """
        Simple get method for returning has_bomb boolean value
        """
        return self.has_bomb

    def get_clicked(self):
        """
        Simple get method for returning clicked boolean value
        """
        return self.clicked

    def get_flagged(self):
        """
        Simple get method for returning flagged boolean value
        """
        return self.flagged

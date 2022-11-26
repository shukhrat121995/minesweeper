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
        self.around = 0
        self.neighbours = []

    def set_neighbours(self, neighbours):
        """
        Receives a list of objects of the Piece class and assign it to the instance so
        that it can access by calling set_number_around function
        """
        self.neighbours = neighbours
        self.set_number_around()

    def get_neighbours(self):
        """
        Return a list of objects of the Piece class
        """
        return self.neighbours

    def set_number_around(self):
        """
        Count the number of bombs around the piece
        """
        counter = 0
        for piece in self.neighbours:
            if piece.get_has_bomb():
                counter += 1
        self.around = counter

    def get_number_around(self):
        """
        Return integer number that represents the number of bombs that surrounds
        this specific piece
        """
        return self.around

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

    def toggle_flag(self):
        """
        Just switch the state of flagged variable
        """
        self.flagged = not self.flagged

    def click(self):
        """
        Handle user's left click
        """
        self.clicked = True

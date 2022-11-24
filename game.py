import os
import pygame


class Game:
    """Initialize the game constructor"""
    def __init__(self, board, screen_size):
        """
        Constructor for the Game class
        """
        self.board = board
        self.screen_size = screen_size
        # width, height
        self.piece_size = self.screen_size[0] // self.board.get_size()[1], \
                          self.screen_size[1] // self.board.get_size()[0]
        self.images = {}
        self.load_images()

    def run(self):
        """Initialize the pygame, grab the screensize and run while event is not QUIT"""
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        """Draw the initial board"""
        top_left = (0, 0)
        for row in range(self.board.get_size()[0]):
            for col in range(self.board.get_size()[1]):
                piece = self.board.get_piece(row, col)
                image = self.get_image(piece)
                self.screen.blit(image, top_left)
                top_left = top_left[0] + self.piece_size[0], top_left[1]
            top_left = 0, top_left[1] + self.piece_size[1]

    def load_images(self):
        """Load images for images folder and store them inside dictionary"""
        for img in os.listdir("images"):
            image = pygame.image.load(f"images/{img}")
            # scale the image
            image = pygame.transform.scale(image, self.piece_size)
            self.images[img.split('.')[0]] = image

    def get_image(self, piece):
        """
        Return empty block or unclicked-bomb images based on piece.get_has_bomb() value
        """
        image_title = "unclicked-bomb" if piece.get_has_bomb() else str(piece.get_number_around())
        return self.images[image_title]

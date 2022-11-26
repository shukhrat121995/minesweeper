import game
import board

size = (12, 7)
probability = 0.5
board = board.Board(size=size, probability=probability)
screen_size = (size[1]*100, size[0]*100)
game = game.Game(board, screen_size)
game.run()

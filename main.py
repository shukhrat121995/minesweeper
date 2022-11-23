import game
import board

size = (9, 9)
probability = 0.5
board = board.Board(size=size, probability=probability)
screen_size = (800, 800)
game = game.Game(board, screen_size)
game.run()

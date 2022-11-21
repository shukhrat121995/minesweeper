import game
import board

size = (9, 9)
board = board.Board(size)
screen_size = (800, 800)
game = game.Game(board, screen_size)
game.run()

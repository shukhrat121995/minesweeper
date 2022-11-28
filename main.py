import game
import board
import pyautogui


size = (12, 7)
probability = 0.1
screen_size = (size[1]*100, size[0]*100)
initial_board = board.Board(size=size, probability=probability)
initial_game = game.Game(initial_board, screen_size)
initial_game.run()

if initial_game.play_again:
    play_again = True
    while play_again and pyautogui.confirm('Play again?') == 'OK':
        new_board = board.Board(size=size, probability=probability)
        new_game = game.Game(new_board, screen_size)
        new_game.run()
        play_again = new_game.play_again

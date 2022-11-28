import game
import board
from input import user_input
import pyautogui

print("* * * Welcome to the MINESWEEPER game * * *")
rows = user_input("Please, enter the number of rows of the board")
cols = user_input("Please, enter the number of columns of the board")

"""
Main menu:
------------------- New Game -----------------------
------------------- Statistics -----------------------
------------------- Quit -----------------------
"""

size = (rows, cols)
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


def user_input(message):
    while True:
        try:
            number = int(input(f'{message} : '))
            if number <= 0:
                print('Please, enter an integer value greater than zero')
                continue
            return number
        except ValueError:
            print('You entered a non integer value, try again.')
            continue

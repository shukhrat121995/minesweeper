import pygame
from game import Game
from board import Board
from constants import PROBABILITY, NEW_GAME, SHOW_STATS, QUIT_GAME, WELCOME_MESSAGE
from input import user_input_rows_and_cols, user_input_option
import pyautogui


def new_game():
    rows = user_input_rows_and_cols("Please, enter the number of rows of the board")
    cols = user_input_rows_and_cols("Please, enter the number of columns of the board")
    size = (rows, cols)
    screen_size = (size[1] * 100, size[0] * 100)  # properly calculate pixels
    gui_confirm = 'OK'

    def close_pygame_ui():
        pygame.display.quit()
        pygame.quit()

    while gui_confirm == 'OK':
        board = Board(size=size, probability=PROBABILITY)
        game = Game(board, screen_size)
        game.run()
        if game.quit:
            close_pygame_ui()
            break
        gui_confirm = pyautogui.confirm('Play again?')
        if gui_confirm == "Cancel":
            close_pygame_ui()
            break


def show_stats():
    pass


print(WELCOME_MESSAGE)

while True:
    print("Please choose from the following options down below: ")
    option = user_input_option("Press << 1 >> to start a new game, press << 2 >> to "
                               "display stats and press << 3 >> to quit the game")

    if option == NEW_GAME:
        new_game()
    elif option == SHOW_STATS:
        pass
    elif option == QUIT_GAME:
        print("Thanks for playing! Good bye :)")
        break

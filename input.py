def user_input_rows_and_cols(message):
    while True:
        try:
            number = int(input(f'{message}: '))
            if number <= 0:
                print('Please, enter an integer value greater than zero')
                continue
            return number
        except ValueError:
            print('You entered a non integer value, try again.')
            continue


def user_input_option(message):
    while True:
        try:
            number = int(input(f'{message}: '))
            if number not in [1, 2, 3]:
                print('Please, enter an integer value either 1, 2 or 3')
                continue
            return number
        except ValueError:
            print('You entered a non integer value, try again.')
            continue

def user_input(message):
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

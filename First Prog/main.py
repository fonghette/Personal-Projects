import random
import time


def dead_state(width, height):
    return [[0 for _ in range(height)] for _ in range(width)]


def random_state(width, height):
    board_random = dead_state(width, height)

    for i in range(height):

        for j in range(width):

            random_number = random.random()

            if random_number >= 0.6:
                cell_state = 1

            else:
                cell_state = 0

            board_random[j][i] = cell_state

    return board_random


def width_state(state):
    return len(state)


def height_state(state):
    return len(state[0])


def render(board):
    line = width_state(board)
    col = height_state(board)

    for i in range(col):
        print('-', end='')

        if i == col - 1:
            print('')

    for i in range(line):

        for j in range(col):

            if j == 0:
                print("|", end='')

            if board[i][j] == 1:
                print(u"\u2588", end='')

            else:
                print(" ", end='')

            if j == col - 1:
                print('|')

    for i in range(col):
        print('-', end='')

        if i == col - 1:
            print('')


def cell_state_in_board(cell_width, cell_height, board):
    return (0 <= cell_width < width_state(board)
            and 0 <= cell_height < height_state(board))


def neighbours_alive(cell_width, cell_height, board):
    counter = 0

    for i in range(3):
        i -= 1

        for j in range(3):
            j -= 1

            if cell_state_in_board(cell_width + i, cell_height + j, board) and (i != 0 or j != 0):
                if board[cell_width + i][cell_height + j] == 1:
                    counter += 1

    return counter


def alive(cell):
    return cell == 1


def next_board_state(board):
    next_board = dead_state(width_state(board), height_state(board))

    for line in range(width_state(board)):

        for col in range(height_state(board)):

            if alive(board[line][col]):

                if neighbours_alive(line, col, board) == 0 or neighbours_alive(line, col, board) == 1:
                    next_board[line][col] = 0

                elif neighbours_alive(line, col, board) == 2 or neighbours_alive(line, col, board) == 3:
                    next_board[line][col] = 1

                else:
                    next_board[line][col] = 0

            else:

                if neighbours_alive(line, col, board) == 3:
                    next_board[line][col] = 1

                else:
                    next_board[line][col] = 0

    return next_board


def unit_test_1():
    init_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    expected_next_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    actual_next_state1 = next_board_state(init_state1)

    if expected_next_state1 == actual_next_state1:
        print("PASSED 1")
    else:
        print("FAILED 1!")
        print("Expected:")
        render(expected_next_state1)
        print("Actual:")
        render(actual_next_state1)


def unit_test_2():
    init_state2 = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    expected_next_state2 = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    actual_next_state2 = next_board_state(init_state2)

    if expected_next_state2 == actual_next_state2:
        print("PASSED 2")
    else:
        print("FAILED 2!")
        print("Expected:")
        render(expected_next_state2)
        print("Actual:")
        render(actual_next_state2)


def unit_test_3():
    init_state3 = [
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
    ]
    expected_next_state3 = [
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1]
    ]
    actual_next_state3 = next_board_state(init_state3)

    if expected_next_state3 == actual_next_state3:
        print("PASSED 3")
    else:
        print("FAILED 3!")
        print("Expected:")
        render(expected_next_state3)
        print("Actual:")
        render(actual_next_state3)


def eternal_life(initial_state):
    render(initial_state)
    board = initial_state

    while True:
        board = next_board_state(board)
        render(board)
        time.sleep(0.03)


def load_initial_state(file_name):

    file = open(file_name)
    content = file.read()
    len_tot = len(content)

    print(len_tot)
    i = 0

    while content[i] != '\n':
        i += 1

    height = i
    width = content.count('\n') + 1

    board = dead_state(width, height)

    counter_width = 0
    counter_height = 0

    for i in range(len(content)):

        if content[i] == '0' or content[i] == '1':
            board[counter_width][counter_height] = int(content[i])
            counter_height += 1

        elif content[i] == '\n':
            counter_height = 0
            counter_width += 1

    return board


def main():
    # width = 20
    # height = 100
    # board = random_state(width, height)

    # render(board) passed!
    # render(next_board_state(board)) passed!

    # unit_test_1() passed!
    # unit_test_2() passed!
    # unit_test_3() passed!

    eternal_life(load_initial_state("glider.txt"))


main()

import copy
import sys

import numpy

from source.utils import read_csv, print_if_verbose


def into_boards(raw_input):
    boards = []
    current_board = []
    for element in raw_input:
        if element == '':
            boards.append(current_board)
            current_board = []
        else:
            current_board.append(row_to_int_list(element))
    return boards


def parse(raw_input):
    game = string_to_int_list(raw_input.pop(0), ',')
    boards = into_boards(raw_input[1:])
    return game, boards


def string_to_int_list(input_string, separator):
    return list(map(lambda x: int(x), input_string.split(separator)))


def row_to_int_list(input_string):
    return list(map(lambda x: int(x), input_string.split()))


def is_winner(board):
    win = False
    for row in board:
        if row.count(-1) == len(row):
            win = True
    for i in range(len(board)):
        column = [row[i] for row in board]
        if column.count(-1) == len(column):
            win = True
    return win


def play(board, game):
    play_board = copy.deepcopy(board)
    wins_in_steps = 0
    for number in game:
        play_one_round(play_board, number)
        wins_in_steps += 1
        if is_winner(play_board):
            break
    return wins_in_steps


def play_one_round(board, number):
    for row in board:
        for index, field in enumerate(row):
            if field == number:
                row[index] = -1


def sum_unmarked(board, game):
    board_list = []
    for row in board:
        board_list = board_list + row
    for number in game:
        if number in board_list:
            board_list.remove(number)
    unmarked_sum = sum(board_list)
    return unmarked_sum


def day_4(input_path, verbose=False):
    raw_input = read_csv(input_path)
    game, boards = parse(raw_input)
    print_if_verbose(f"Successfully parsed input data!", verbose)
    print_if_verbose(f"Game: {game}", verbose)
    print_if_verbose(f"Boards: {len(boards)}", verbose)

    fastest_winner_board = None
    fastest_wins_in_steps = sys.maxsize

    slowest_winner_board = None
    slowest_wins_in_steps = 0

    for board in boards:
        wins_in_steps = play(board, game)
        print_if_verbose(f"Board {boards.index(board)} wins in {wins_in_steps} steps", verbose)
        if wins_in_steps < fastest_wins_in_steps:
            fastest_winner_board = board
            fastest_wins_in_steps = wins_in_steps
            print_if_verbose(f"The fastest winner board is now board {boards.index(board)} "
                             f"and wins in {fastest_wins_in_steps} steps", verbose)
            print_if_verbose(f"The board looks like this: {fastest_winner_board}", verbose)
        if wins_in_steps > slowest_wins_in_steps:
            slowest_winner_board = board
            slowest_wins_in_steps = wins_in_steps
            print_if_verbose(f"The slowest winner board is now board {boards.index(board)} "
                             f"and wins in {slowest_wins_in_steps} steps", verbose)
            print_if_verbose(f"The board looks like this: {slowest_winner_board}", verbose)

    fastest_winner_board_unmarked_sum = sum_unmarked(fastest_winner_board, game[0:fastest_wins_in_steps])
    fastest_winner_board_score = fastest_winner_board_unmarked_sum * game[fastest_wins_in_steps-1]

    slowest_winner_board_unmarked_sum = sum_unmarked(slowest_winner_board, game[0:slowest_wins_in_steps])
    slowest_winner_board_score = slowest_winner_board_unmarked_sum * game[slowest_wins_in_steps-1]
    return fastest_winner_board_score, slowest_winner_board_score



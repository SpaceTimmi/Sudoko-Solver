# VAL is any Natural from [1, 9]
# Position is a list of size 81 and can contain any VAL

# Data Defintions and imports

import numpy as np
from collections import Counter

ALL_VALS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = False


# Boards
# Boards are represented with a lists that can contain any natural in ALL_Vals or B. It is an 81 element list representing all 81 positions
# in  sudoku board
BD1 = [B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B]

BD2 = [2, 7, 4, B, 9, 1, B, B, 5,
       1, B, B, 5, B, B, B, 9, B,
       6, B, B, B, B, 3, 2, 8, B,
       B, B, 1, 9, B, B, B, B, 8,
       B, B, 5, 1, B, B, 6, B, B,
       7, B, B, B, 8, B, B, B, 3,
       4, B, 2, B, B, B, B, B, 9,
       B, B, B, B, B, B, B, 7, B,
       8, B, B, 3, 4, 9, B, B, B]

# solution to 2
BD2s = [2, 7, 4, 8, 9, 1, 3, 6, 5,
        1, 3, 8, 5, 2, 6, 4, 9, 7,
        6, 5, 9, 4, 7, 3, 2, 8, 1,
        3, 2, 1, 9, 6, 4, 7, 5, 8,
        9, 8, 5, 1, 3, 7, 6, 4, 2,
        7, 4, 6, 2, 8, 5, 9, 1, 3,
        4, 6, 2, 7, 5, 8, 1, 3, 9,
        5, 9, 3, 6, 1, 2, 8, 7, 4,
        8, 1, 7, 3, 4, 9, 5, 2, 6]

BD3 = [5, B, B, B, B, 4, B, 7, B,
       B, 1, B, B, 5, B, 6, B, B,
       B, B, 4, 9, B, B, B, B, B,
       B, 9, B, B, B, 7, 5, B, B,
       1, 8, B, 2, B, B, B, B, B,
       B, B, B, B, B, 6, B, B, B,
       B, B, 3, B, B, B, B, B, 8,
       B, 6, B, B, 8, B, B, B, 9,
       B, B, 8, B, 7, B, B, 3, 1]

# solution to 3
BD3s = [5, 3, 9, 1, 6, 4, 8, 7, 2,
        8, 1, 2, 7, 5, 3, 6, 9, 4,
        6, 7, 4, 9, 2, 8, 3, 1, 5,
        2, 9, 6, 4, 1, 7, 5, 8, 3,
        1, 8, 7, 2, 3, 5, 9, 4, 6,
        3, 4, 5, 8, 9, 6, 1, 2, 7,
        9, 2, 3, 5, 4, 1, 7, 6, 8,
        7, 6, 1, 3, 8, 2, 4, 5, 9,
        4, 5, 8, 6, 7, 9, 2, 3, 1]

# no solution
BD4 = [1, 2, 3, 4, 5, 6, 7, 8, B,
       B, B, B, B, B, B, B, B, 2,
       B, B, B, B, B, B, B, B, 3,
       B, B, B, B, B, B, B, B, 4,
       B, B, B, B, B, B, B, B, 5,
       B, B, B, B, B, B, B, B, 6,
       B, B, B, B, B, B, B, B, 7,
       B, B, B, B, B, B, B, B, 8,
       B, B, B, B, B, B, B, B, 9]


# Rows is a list of lists that  refers to each row in a standard 9x9 sudoku board with 0 to 80 representing each position
# 0 1 2 3 4 5 6 7 8

# Cols is a list of lists refers to each column in a standard 9x9 sudoku board with 0 to 80 representing each positon
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# Boxes is a list of lists that refers to each individual 3x3 box in a 9x9 sudoku board
# 0 1 2
# 3 4 5
# 6 7 8

ROWS = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16, 17],
        [18, 19, 20, 21, 22, 23, 24, 25, 26],
        [27, 28, 29, 30, 31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40, 41, 42, 43, 44],
        [45, 46, 47, 48, 49, 50, 51, 52, 53],
        [54, 55, 56, 57, 58, 59, 60, 61, 62],
        [63, 64, 65, 66, 67, 68, 69, 70, 71],
        [72, 73, 74, 75, 76, 77, 78, 79, 80]]

COLS = [[0, 9, 18, 27, 36, 45, 54, 63, 72],
        [1, 10, 19, 28, 37, 46, 55, 64, 73],
        [2, 11, 20, 29, 38, 47, 56, 65, 74],
        [3, 12, 21, 30, 39, 48, 57, 66, 75],
        [4, 13, 22, 31, 40, 49, 58, 67, 76],
        [5, 14, 23, 32, 41, 50, 59, 68, 77],
        [6, 15, 24, 33, 42, 51, 60, 69, 78],
        [7, 16, 25, 34, 43, 52, 61, 70, 79],
        [8, 17, 26, 35, 44, 53, 62, 71, 80]]

BOXES = [[0, 1, 2, 9, 10, 11, 18, 19, 20],
         [3, 4, 5, 12, 13, 14, 21, 22, 23],
         [6, 7, 8, 15, 16, 17, 24, 25, 26],
         [27, 28, 29, 36, 37, 38, 45, 46, 47],
         [30, 31, 32, 39, 40, 41, 48, 49, 50],
         [33, 34, 35, 42, 43, 44, 51, 52, 53],
         [54, 55, 56, 63, 64, 65, 72, 73, 74],
         [57, 58, 59, 66, 67, 68, 75, 76, 77],
         [60, 61, 62, 69, 70, 71, 78, 79, 80]]

# Units represent all the possible locations where no duplicate number is supposed to be found.
UNITS = ROWS + COLS + BOXES

# !!! Add test for all functions in the tests.py file.

# Board -> Board, Boolean
# Takes a board as input and returns a solved board or False if the board is unsolvable.

# The algorith checks if the given board has been solved, if yes, it returns the solved board
# else it sends current board to build_next_boards which returns a list all possible valid
# boards from the current position and sends them to solve_lob.


def solve_board(board):
    if solved(board):
        return board
    else:
        next_boards = build_next_boards(board)
        return solve_lob(next_boards)

# (ListOf Boards) -> (ListOf Boards)
# Takes a list of possible next boards from a position and sends only the valid boards to solve.

# The algorithm here checks if the first board in the list of boards leads to a solution
# if it does it just returns the solution else it will the check the  other valid boards.
# We can assume all boards that get to solve_lob is valid board.
def solve_lob(lob):
    if len(lob) == 0:
        return False
    else:
        check = solve_board(lob[0])
        if check is not False:
            return check
        else:
            return solve_lob(lob[1::])


# Board -> Boolean
# produce true if given board has been solved, otherwise produce false.

# The algorithm loops through all the positions of a given board and returns true if all
# positions have been filled i.e has a natural else it returns False.
def solved(board):
    return all(str(elem).isdigit() for elem in board)

# Board -> (ListOf Boards)
# produce the next list of valid boards from a given board.

def build_next_boards(board):
    position = find_blank_position(board)  # board -> position
    # position, board -> (ListOf Boards)
    all_boards = fill_all(position, board)
    result = valid_boards(all_boards)  # (listOf Boards) -> (ListOf Boards)
    return result


# Helper functions for build_next_boards:
def find_blank_position(board):
    for index, elem in enumerate(board):
        if elem is False:
            return index
    # Assuming that all boards that get to find_blank_position has atleast one False in the board.


# Loops through 1 to 9 and adds each value [1,9] to the given position for 9 new boards.
def fill_all(position, board):
    lob = []
    for i in range(1, 10):
        new_board = board.copy()
        new_board[position] = i
        lob.append(new_board)
    return lob


def valid_boards(lob):
	confirmed_boards = list()
	for board in lob:
		board_arr = np.array(board)
		if no_duplicates(board_arr) is True: confirmed_boards.append(board_arr)
	return confirmed_boards


def no_duplicates(board):
	count = 0
	for unit in UNITS:
		pos = board[unit] 
		consideration = [elem for elem in pos if not isinstance(elem, bool)] 
		result = [elem for elem, count in Counter(consideration).items() if not count > 1]
		if len(result) == len(consideration) : count+= 1
	if len(board) == count: return True
	else: return False

result = solve_board(BD2)
print(result)
print(BD2s)
	
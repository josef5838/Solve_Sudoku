from typing import List, Tuple, Optional

def is_valid(board: List[List[int]], row: int, col: int, num: int) -> bool:
    # Check if the number is already in the current row
    if num in board[row]:
        return False

    # Check if the number is already in the current column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is already in the 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty_location(board: List[List[int]]) -> Optional[Tuple[int, int]]:
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(board: List[List[int]]) -> bool:
    empty_location = find_empty_location(board)
    if not empty_location:
        return True  # Puzzle solved

    row, col = empty_location

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack

    return False

# The initial Sudoku board
sudoku_board = [
    [0, 0, 1, 0, 9, 0, 2, 7, 0],
    [0, 0, 9, 0, 0, 2, 0, 5, 0],
    [2, 0, 0, 0, 0, 3, 0, 0, 0],
    [3, 0, 0, 0, 1, 4, 0, 0, 2],
    [0, 8, 0, 0, 0, 0, 0, 4, 0],
    [1, 0, 0, 2, 8, 0, 0, 0, 5],
    [0, 0, 0, 9, 0, 0, 0, 0, 7],
    [0, 1, 0, 3, 0, 0, 9, 0, 0],
    [0, 4, 6, 0, 7, 0, 5, 0, 0]
]

# Solve the puzzle
if solve_sudoku(sudoku_board):
    solved_board = sudoku_board
else:
    solved_board = None

solved_board
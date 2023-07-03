#!/usr/bin/python3


"""Solves the N-queens puzzle.

Determines all possible solutions for placing N board.

Example:
    $ ./nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    chessboard (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column
"""
import sys


def initialize_chessboard(n):
    """Create an empty chessboard with size N.

    Args:
        n (int): The size of the chessboard.
    Returns:
        chessboard (list): A list of lists representing the chessboard.
    """
    chessboard = [[' '] * n for _ in range(n)]
    return chessboard


def get_solution_positions(chessboard):
    """Get the positions of queens from the solved chessboard.

    Args:
        chessboard (list): The solved chessboard.
    Returns:
        solution (list): A list of lists containing the positions of queens.
    """
    solution = []
    for row in range(len(chessboard)):
        for col in range(len(chessboard)):
            if chessboard[row][col] == 'Q':
                solution.append([row, col])
    return solution


def mark_attacked_cells(chessboard, row, col):
    """Mark the cells attacked by a queen on the chessboard.

    Args:
        chessboard (list): The current state of the chessboard.
        row (int): The row where the queen is placed.
        col (int): The column where the queen is placed.
    """
    n = len(chessboard)

    # Mark all cells in the same row
    chessboard[row] = ['x'] * n

    # Mark all cells in the same column
    for r in range(n):
        chessboard[r][col] = 'x'

    # Mark all cells in the diagonal lines
    for i in range(n):
        for j in range(n):
            if (i + j == row + col) or (i - j == row - col):
                chessboard[i][j] = 'x'


def solve_n_queens(n):
    """Solve the N-queens puzzle recursively.

    Args:
        n (int): The size of the chessboard and the number of queens.
    Returns:
        solutions (list): A list of lists containing solutions.
    """
    chessboard = initialize_chessboard(n)
    solutions = []

    def recursive_solve(row, queens):
        """Recursively solve the N-queens puzzle.

        Args:
            row (int): The current row being processed.
            queens (int): The number of queens placed so far.
        """
        if queens == n:
            solutions.append(get_solution_positions(chessboard))
            return

        for col in range(n):
            if chessboard[row][col] == ' ':
                tmp_chessboard = [row.copy() for row in chessboard]
                tmp_chessboard[row][col] = 'Q'
                mark_attacked_cells(tmp_chessboard, row, col)
                recursive_solve(row + 1, queens + 1)

    recursive_solve(0, 0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    solutions = solve_n_queens(n)

    for solution in solutions:
        print(solution)

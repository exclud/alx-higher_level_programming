#!/usr/bin/python3
"""Import Sys module"""


import sys

def solve_nqueens(N):
    """
    Solves the N-queens problem and prints all possible solutions.

    Args:
        N (int): The number of queens and the size of the chessboard.
    """
    def is_safe(board, row, col):
        """
        Checks if it's safe to place a queen at the specified position.

        Args:
            board (list): The chessboard representation.
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check if there is a queen in the upper-left diagonal
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check if there is a queen in the upper-right diagonal
        i = row - 1
        j = col + 1
        while i >= 0 and j < N:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backtrack(board, row):
        """
        Backtracking function to find all solutions.

        Args:
            board (list): The current state of the chessboard.
            row (int): The current row to place the queen.
        """
        if row == N:
            # All queens have been placed, print the solution
            for r in board:
                print(' '.join(r))
            print()
            return

        for col in range(N):
            if is_safe(board, row, col):
                # Place the queen
                board[row][col] = 'Q'
                # Recur for the next row
                backtrack(board, row + 1)
                # Remove the queen (backtracking)
                board[row][col] = '.'

    # Check the validity of N
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [['.' for _ in range(N)] for _ in range(N)]

    # Start solving the N-queens problem
    backtrack(board, 0)


# Run the program
if __name__ == "__main__":
    solve_nqueens(N)

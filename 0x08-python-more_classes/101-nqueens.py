"""Import module"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at the given position on the board.

    Args:
        board (list[list[int]]): The chessboard representation.
        row (int): The row index.
        col (int): The column index.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the current row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """
    Recursive utility function to solve the N queens problem.

    Args:
        board (list[list[int]]): The chessboard representation.
        col (int): The current column index.
        N (int): The size of the chessboard.
        solutions (list[list[str]]): List to store the solutions.

    Returns:
        None
    """
    if col == N:
        solution = [''.join('Q' if cell else '.' for cell in row)
                    for row in board]
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, N, solutions)
            board[i][col] = 0


def solve_nqueens(N):
    """
    Solve the N queens problem and print the solutions.

    Args:
        N (str): The size of the chessboard.

    Returns:
        None
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print('\n'.join(solution))
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])

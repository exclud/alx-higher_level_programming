import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True

def solve_n_queens(board, col, solutions):
    """
    Solve the N-queens problem using backtracking.
    """
    if col >= len(board):
        # Found a solution, add it to the solutions list
        solutions.append(["".join(row) for row in board])
        return

    for row in range(len(board)):
        if is_safe(board, row, col):
            # Place a queen at board[row][col]
            board[row][col] = "Q"

            # Recur for the next column
            solve_n_queens(board, col + 1, solutions)

            # Remove the queen from board[row][col] (backtrack)
            board[row][col] = "."

def print_solutions(solutions):
    """
    Print the solutions to the N-queens problem.
    """
    for solution in solutions:
        for row in solution:
            print(row)
        print()

def nqueens(N):
    """
    Solve the N-queens problem for a given N.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [["."] * N for _ in range(N)]
    solutions = []

    solve_n_queens(board, 0, solutions)

    print_solutions(solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

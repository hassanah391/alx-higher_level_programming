#!/usr/bin/python3
"""Module to solve the N Queens problem."""
import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """Solve the N Queens problem and return all solutions."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions


def solve_nqueens_util(board, col, n, solutions):
    """Utility function to solve N Queens problem using backtracking."""
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0


def print_solutions(solutions):
    """Print all solutions."""
    for solution in solutions:
        print(solution)


def main():
    """Main function to handle input and solve the N Queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()

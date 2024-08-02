#!/usr/bin/python3
""" nqueen module """
import sys


def nqueens():
    """ nqueen function """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    def isSafe(board, row, col):
        """ isSafe function """
        for i in range(col):
            if (board[i] == row or board[i] - i == row - col or
                    board[i] + i == row + col):
                return False
        return True

    def solve(board, col):
        """ solve function """
        if col == n:
            print(str([[i, board[i]] for i in range(n)]))
            return
        for i in range(n):
            if isSafe(board, i, col):
                board[col] = i
                solve(board, col + 1)

    solve([0 for i in range(n)], 0)


if __name__ == "__main__":
    nqueens()

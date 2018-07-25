"""Program to print all N-Queen Solutions in N * N board."""

QUEEN = "\u265B"        # unicode of chess queen-symbol
N = 8
x = 1


def is_safe(board, row, col):
    """Checking if a queen can be placed on board[row][col]."""

    # Check this row on left size
    for i in range(col):
        if board[row][i] == QUEEN:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False

    # Check lower diagonal on left size
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False

    return True


def n_queen_solution(board, col):
    """Function that return the solution if there any."""
    res = False
    global x

    if col >= N:
        print(x, ": ")
        for i in range(N):
            for j in range(N):
                print(board[i][j], end="  ")
            print()
        print()
        x += 1
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = QUEEN

            # if only one solution needed then use this block instead of next line.
            # Also return False in last line in place of return res.
            # >>
            # if n_queen_solution(board, col + 1, n):
            #     return True

            res = n_queen_solution(board, col + 1) or res

            board[i][col] = '_'         # backtrack

    return res


def n_queen():
    """Program that print solution if exist."""
    board = [['_' for _ in range(N)] for _ in range(N)]
    y = n_queen_solution(board, 0)

    if not y:
        print("No solution exist!")


if __name__ == '__main__':
    n_queen()

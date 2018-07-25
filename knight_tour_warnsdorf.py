"""Solution of Knight tour problem using Warnsdorf's rule."""

import sys

sys.setrecursionlimit(10000)            # use this for larger values of N

N = 8
x_initial, y_initial = 0, 0


def is_safe(board, x, y):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


def solve_tour():
    """Function to find one of the feasible knight tours."""
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[x_initial][y_initial] = 0

    # all 8 possible moves of knight at any given position
    jumps = ((-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1))
    z = find_tour(board, x_initial, y_initial, 1, jumps)

    if not z:
        print("No solution exist!")


def find_tour(board, x, y, move_k, jumps):
    """Recursive function that return whether a solution exist from the given position."""
    if move_k == N * N:
        for i in range(N):
            for j in range(N):
                print("%3d" % board[i][j], end=" ")
            print()
        return True

    sorted_moves = min_degree(board, x, y, jumps)

    for x_next, y_next in sorted_moves:
        board[x_next][y_next] = move_k

        if find_tour(board, x_next, y_next, move_k + 1, jumps):
            return True

        board[x_next][y_next] = -1          # backtrack

    return False


def min_degree(board, x, y, jumps):
    """Function that return the list of sorted moves in increasing order of degree."""
    empty_neighbours = []

    for jump in jumps:
        x_next = x + jump[0]
        y_next = y + jump[1]

        if is_safe(board, x_next, y_next):
            empty_neighbours.append([x_next, y_next])

    sorted_moves = sorted(empty_neighbours, key=lambda c: sum(
        [is_safe(board, c[0] + j[0], c[1] + j[1]) for j in jumps]))
    return sorted_moves


if __name__ == "__main__":
    solve_tour()

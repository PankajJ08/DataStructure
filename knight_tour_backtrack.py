"""Program to print knight-tour solution in N * N board using Backtracking."""

N = 8


def is_safe(board, x, y):
    """Function to check whether the square is safe to visit or not."""
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


def knight_tour():
    """Function to find knight-tour solution."""
    board = [[-1 for _ in range(N)]for _ in range(N)]
    board[0][0] = 0

    # all 8 possible moves of knight at any given position
    # Don't change the order, it is optimal.
    jumps = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))
    z = find_tour(board, 0, 0, 1, jumps)

    if not z:
        print("No solution exist.")


def find_tour(board, x, y, move, jumps):
    """Function that check for knight tour for a given square."""
    if move == N * N:
        for i in range(N):
            for j in range(N):
                print("%3d" % board[i][j], end=" ")
            print()
        return True

    for jump in jumps:
        x_next = x + jump[0]
        y_next = y + jump[1]

        if is_safe(board, x_next, y_next):
            board[x_next][y_next] = move

            if find_tour(board, x_next, y_next, move + 1, jumps):
                return True

            board[x_next][y_next] = -1          # backtrack

    return False


if __name__ == "__main__":
    knight_tour()

from itertools import count


def create_matrix(side):
    if side <= 0:
        raise ValueError("side size must be greater than zero")

    matrix = [[None] * side for _ in range(side)]
    row = col = (side - 1) // 2
    counter = count(1)
    matrix[row][col] = next(counter)

    def move(x, y, *, times=1):
        nonlocal row, col
        for _ in range(times):
            row += x
            col += y
            matrix[row][col] = next(counter)

    for side_limit in range(2, side + 1):
        times = side_limit - 1
        if side_limit % 2 == 0:
            move(0, 1)
            move(1, 0, times=times)
            move(0, -1, times=times)
        else:
            move(0, -1)
            move(-1, 0, times=times)
            move(0, 1, times=times)

    return matrix

def create_matrix(side):
    matrix = [[None] * side for _ in range(side)]
    row = col = (side - 1) // 2
    nums_iter = iter(range(1, side ** 2 + 1))
    matrix[row][col] = next(nums_iter)

    for side_limit in range(2, side + 1):
        if side_limit % 2 == 0:
            col += 1
            matrix[row][col] = next(nums_iter)

            for _ in range(side_limit - 1):
                row += 1
                matrix[row][col] = next(nums_iter)

            for _ in range(side_limit - 1):
                col -= 1
                matrix[row][col] = next(nums_iter)
        else:
            col -= 1
            matrix[row][col] = next(nums_iter)

            for _ in range(side_limit - 1):
                row -= 1
                matrix[row][col] = next(nums_iter)

            for _ in range(side_limit - 1):
                col += 1
                matrix[row][col] = next(nums_iter)

    return matrix

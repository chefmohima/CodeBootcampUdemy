def spiral_matrix(n):
    # build blank matrix with 0s
    matrix = []
    max_count = n ** 2
    for i in range(n):
        sublist = []
        for j in range(n):
            sublist.append(0)
        matrix.append(sublist)
    count = 0
    first_row, first_col = 0, 0
    last_row, last_col = n, n
    i, j = 0, 0

    while first_row <= last_row and first_col <= last_col:
        # move right
        for j in range(first_col, last_col):
            if matrix[i][j] == 0:
                count += 1
                matrix[i][j] = count

        first_row += 1

        # move down
        for i in range(first_row, last_row):
            if matrix[i][j] == 0:
                count += 1
                matrix[i][j] = count

        last_col -= 1

        # move left
        for j in range(last_col, first_col - 1, -1):
            if matrix[i][j] == 0:
                count += 1
                matrix[i][j] = count
        last_row -= 1

        # move up
        for i in range(last_row, first_row - 1, -1):
            if matrix[i][j] == 0:
                count += 1
                matrix[i][j] = count

        first_col += 1
    return matrix


def print_matrix(two_d_list):
    for row in two_d_list:
        print(row)


test_list = spiral_matrix(5)
print_matrix(test_list)

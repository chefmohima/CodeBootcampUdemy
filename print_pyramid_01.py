# print a pyramid like this
# level = 5
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


def print_pyramid(levels):
    # notice the pattern itself has SPACES
    # cells per row = number of pattern in last row
    # 1 -> 3 -> 5 -> 7 ->....which is an A.P, nth term=a+(n-1)*d
    cells_per_row = 1 + (levels - 1) * 2
    for level in range(1, levels+1):
        # form pattern first
        length_of_pattern = 1 + (level - 1) * 1
        pattern = ''
        for i in range(length_of_pattern):
            pattern += "*_"
        pattern = pattern.rstrip('_')
        l = len(pattern)

        spaces_per_row = cells_per_row - l
        # start to print
        print('_' * (spaces_per_row // 2), end='')
        print(pattern, end='')
        print('_' * (spaces_per_row // 2), end='')
        print()

print_pyramid(5)

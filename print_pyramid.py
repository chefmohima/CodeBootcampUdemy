# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a step shape
# with N levels using the # character.  Make sure the
# step has spaces on the right hand side!
# --- Examples
#   steps(2)
#       '# '
#       '##'
#   steps(3)
#       '#  '
#       '## '
#       '###'
#   steps(4)
#       '#   '
#       '##  '
#       '### '
#       '####'

def print_pyramid(num_of_levels):
    cells_per_row = 1+(num_of_levels-1)*2
    for level in range(1, num_of_levels+1):
        num_of_pattern = 1+(level-1)*2
        num_of_spaces = cells_per_row - num_of_pattern
        space_per_side = num_of_spaces//2
        print(' ' * space_per_side, end='')
        print("#" * num_of_pattern, end='')
        print(' ' * space_per_side, end='')
        print('')

print_pyramid(4)

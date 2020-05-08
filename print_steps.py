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




def print_steps(num_of_steps):
    for i in range(num_of_steps):
        step_to_print = "#" * (i+1)
        print(step_to_print)
    return


print_steps(2)
print_steps(3)
print_steps(4)


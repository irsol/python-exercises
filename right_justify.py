#Function takes a string named s as a parameter.
#Prints the string so the last letter of the string in column 70.


def right_justify(s):
    max_length = 70
    space = ' '
    num_length = max_length - len(s)
    s = space * num_length + s
    print(s)

right_justify('monty')
right_justify('cat')
right_justify('dddddfffffffggggggg')
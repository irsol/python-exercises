def print_grid():

    print('+', '-' * 4, '+', '-' * 4, '+') 
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('+', '-' * 4, '+', '-' * 4, '+') 
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('+', '-' * 4, '+', '-' * 4, '+') 

#print_grid()


def grid_print(rows, columns):
    #h_line = ("+ " + "- " * 4) * rows
    #v_line = ("| " + " " * 8) * v_lines

    #print(h_line + "\n" + v_line)

    cell_width = 4
    cell_height = 4
    h_line = ("+" + "-" * cell_width) * columns + "+"
    v_line = ("|" + " " * cell_width) * (columns + 1)

    for i in range(rows):
        print(h_line)

        for j in range(cell_height):
            print(v_line)

    print(h_line)

grid_print(2, 5)


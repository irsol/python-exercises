def print_grid(rows, columns):

    cell_height = 3
    cell_width = 3
    v_line = ("|")
    h_line = ("-")
    
    for i in range(rows):
        print(h_line)

        for j in range(columns):
            print(v_line)


print_grid(2, 4)

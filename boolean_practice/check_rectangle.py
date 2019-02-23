# Function checks if the given points make rectangle.


def check_rect(points):
    # Check if in the list points four elements
    if len(points) == 4:
        a, b, c, d = points

        if (a[0] == b[0] and a[1] == d[1] and b[0] == a[0] and b[1] == c[1] and
                c[0] == d[0] and c[1] == b[1] and d[0] == c[0] and d[1] == a[1]):
            return True

    return False


# List of points
rectangle = [[1, 2], [1, 4], [5, 4], [5, 2]]

print("Yes, this is rectangle!" if check_rect(rectangle) is True else "No!")

# Function checks if the given points make rectangle.
from nose.tools import *


def check_rect(points):
    # Check if in the list points four elements
    if len(points) == 4:
        a, b, c, d = points

        if len(a) == 2 and len(b) == 2 and len(c) == 2 and len(d) == 2:
            if (a[0] == b[0] and a[1] == d[1] and b[0] == a[0] and b[1] == c[1] and
                    c[0] == d[0] and c[1] == b[1] and d[0] == c[0] and d[1] == a[1]):
                return True

    return False


def calc_area(rectangle):
    if len(rectangle) == 4:
        a, b, c, d = rectangle
        area = abs(a[1] - b[1]) * abs(b[0] - c[0])
        return area

    return -1


def test_check_rect():
    rectangle = [[1, 2], [1, 4], [5, 4], [5, 2]]
    assert_true(check_rect(rectangle))

    rectangle = [[], [1, 4], [5, 4], [5, 2]]
    assert_false(check_rect(rectangle))

    rectangle = [[1, 2], [1, 4]]
    assert_false(check_rect(rectangle))

    rectangle = [[1, 1], [1, 4], [5, 4], [5, 2]]
    # assert check_rect(rectangle)
    assert_false(check_rect(rectangle))

    print('Test passed')


def test_calc_area():
    rectangle = [[0, 0], [0, 0], [0, 0], [0, 0]]
    assert_equal(calc_area(rectangle), 0)

    rectangle = [[0, 0], [0, 0]]
    assert_equal(calc_area(rectangle), -1)

    rectangle = [[1, 2], [1, 4], [5, 4], [5, 2]]
    assert_equal(calc_area(rectangle), 8)

    rectangle = [[1, 1], [1, 2], [2, 2], [2, 1]]
    assert_equal(calc_area(rectangle), 1)

    print('Test passed')


if __name__ == '__main__':
    test_check_rect()
    test_calc_area()

    # List of points
    rectangle = [[1, 2], [1, 4], [5, 4], [5, 2]]

    print("Yes, this is rectangle!" if check_rect(rectangle) is True else "No!")

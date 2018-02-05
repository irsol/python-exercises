
def evaluate(x, y):
    if x and y >= 1:
        return True
    elif x and y <= 0:
        return False
    elif x == 1 and y == 0:
        print(None)
    elif x == 0 and y == 1:
        print(None)

evaluate(0, 0)


def evaluate(x, y):
    if x == 'True' and y == 'True':
        return True
evaluate(1, 1)

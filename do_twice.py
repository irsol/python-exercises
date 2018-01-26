# do_tvice takes a function object as an argument
# and calls it twice


def do_twice(f, k):  # f=print_spam, k=2
    f(k)  # print_spam()
    f(k)


def print_spam(v):
    print('spam')


do_twice(print_spam, 1)


# Runs a function twice
# func: functional object
# arg: argument passed to the function
def do_twice(func, arg):

    func(arg)
    func(arg)
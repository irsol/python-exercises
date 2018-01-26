# Runs the function twice.
def do_twice(func, arg):

    func(arg)
    func(arg)


# Prints the argument twice.
def print_twice(arg):

    print(arg)
    print(arg)


# Runs the function four times.
def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_twice(print_twice, 'spam')
print('')

do_four(print_twice, 'spam')

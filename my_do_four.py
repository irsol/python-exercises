

# f: a function object, k: a value
# Calls the function twice, passing the value as an argument.
def do_twice(f, k):
    f(k)
    f(k)


# Runs a function four times.
def do_four(f, k):
    do_twice(f, k)
    do_twice(f, k)

do_twice(print, 'cat')
print('')

do_four(print, 'dog')

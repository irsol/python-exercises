

#Creating a function
def hello():
    print('Hello')


def area(width, height):
    return width * height


def print_welcome(name):
    #print Welcome
    print('Welcome', name)

# calling function def hello()
hello()
hello()

# pass the value to the name argument
print_welcome('Fred')

w = 4
h = 5

print('width =', w, 'height =', h, 'area =', area(w, h))
#
#
# Variables in function
# global variable
a = 4


def print_func():
    #local variable
    a = 17
    print('in print_func a =', a)

print_func()
print('a = ', a)


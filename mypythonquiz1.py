 #1: what does the following code do?
def a(b, c, d):
    pass
# The 'def' statement defines a function.
# The 'pass' statement is a null operation.


#2: what is the output of the following code?
print(type([1, 2]))
#  Lists are formed by placing a comma-separated
#list of expressions in square brackets


#3: what gets printed?
def f():
    pass
print(type(f()))
# The argument to the type() call is a return value of
# a function call, which returns None


#4: what should the below code print?
print(type(1J))
#<class 'complex'> or j means complex number
# you can put ‘j’ or ‘J’ after a number to make it imaginary,
# so you can write complex literals

#5: what is the output of the following code?
print(type(lambda: None))
# <class 'function'>
# 'lambda arguments: expression' yields a function object


#6: what is the output of the below program?
a=[1, 2, 3, None, (), [], ]
print(len(a))
# 6
# The trailing comma in the list is ignored, the rest are legitimate values

#7: what gets printed?
print(type(1/2))
# <class 'float'>
#  division of an integer by another integer yields a float

#8: What gets printed?
d = lambda p: p * 2
t = lambda p: p * 3
x = 2
x = d(x)
x = t(x)
x = d(x)
print(x)
# 24
# start with 2, multiply by 2, multiply by 3, multipy by 2

#10: What gets printed?
nums = set([1, 1, 2, 3, 3, 3, 4])
print(len(nums))
# nums is a set, so only unique values are retained.

#11: What gets printed?
x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")
# yes
#  AND is higher precedence than OR in python and is evaluated first

# #12: What gets printed?
x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)
# 3
#  NOT has first precedence, then AND, then OR


#14: What gets printed?
counter = 1


def doLotsOfStuff():
    global counter
    for i in (1, 2, 3):
        counter += 1

doLotsOfStuff()
print(counter)
# 4
#  the counter variable being referenced in the function is the global
# variable defined outside of the function.  Changes to the variable in
# the function affect the original variable.

#16: What gets printed?
print("\x48\x49!")
# HI!
# \x is an escape sequence that means the following 2 digits ares
# a hexadicmal number encoding a character.

#17: What gets printed?
print(0xA + 0xa)
# 20
# 0xA and 0xa are both hexadecimal integer literals representing the decimal
# value 10.  Their sum is 20.


#18: What gets printed?
class parent:
    def __init__(self, param):
        self.v1 = param


class child(parent):
    def __init__(self, param):
        self.v2 = param

obj = child(11)
print(obj.v1 + " " + obj.v2)
#  AttributeError: child instance has no attribute 'v1'.  self.v1 was never
# created as a variable since the parent __init__ was not explicitly called.

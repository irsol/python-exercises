import turtle
bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(length)


#square(bob, 90)
#turtle.mainloop()


# n is a number of polygon sides
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)



#def circle(t, r):
#    c = length * n


#circle(polygon, 10)


polygon(bob, 90, 9)
turtle.mainloop()

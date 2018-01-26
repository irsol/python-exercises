import turtle
bob = turtle.Turtle()
bob.fd(100)
bob.lt(90)
bob.fd(100)

bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

for i in range(4):
    bob.fd(100)
    bob.lt(90)

for i in range(4):
    print('Hello!')

print(bob)
turtle.mainloop()

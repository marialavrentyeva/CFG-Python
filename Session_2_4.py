import turtle

def square():
    side_length = 100
    angle = 90
    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)

square()
turtle.forward(150)
square()
turtle.done()
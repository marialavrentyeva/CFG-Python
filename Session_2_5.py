import turtle
def triangle(length, colour):
    angle = 120
    turtle.color(colour)
    turtle.begin_fill()
    turtle.end_fill()
    for side in range(3):
        turtle.forward(length)
        turtle.right(angle)

    turtle.done()

triangle(50, "red")
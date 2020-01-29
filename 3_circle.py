import turtle
def circle():
    turtle.shape('turtle')
    i = 0
    while i < 360:
        turtle.forward(1)
        turtle.left(1)
        i = i+1
    pass

if __name__== "__main__":
    circle()
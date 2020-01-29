import turtle

turtle.shape('turtle')
def rect_spiral():
    i = 0
    b = 10
    while i < 5:
        turtle.forward(b)
        turtle.left(90)
        b = b+10


    pass

if __name__== "__main__":
    rect_spiral()
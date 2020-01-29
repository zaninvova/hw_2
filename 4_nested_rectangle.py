import turtle

turtle.shape('turtle')
def nested_rectangle():
    i = 0
    b = 10
    while i < 10:
        turtle.forward(b)
        turtle.left(90)
        b = b+10


    pass

if __name__== "__main__":
    nested_rectangle()
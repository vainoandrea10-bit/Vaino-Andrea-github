import turtle
screen = turtle.Screen()
screen.setup(width=400, height=300)
screen.title("Pixel Art")

turtle_pixel = turtle.Turtle()
turtle_pixel.speed(1)

def design(x, y, color, pixel_size):
    turtle_pixel.penup()
    turtle_pixel.goto(x, y)
    turtle_pixel.pendown()
    turtle_pixel.fillcolor(color)
    turtle_pixel.begin_fill()
    for i in range(4):
        turtle_pixel.forward(pixel_size)
        turtle_pixel.right(90)
    turtle_pixel.end_fill()
design(0,0,"red",50)

screen.mainloop()

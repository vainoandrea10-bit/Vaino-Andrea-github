import turtle

screen = turtle.Screen()
screen.setup(width=400, height=300)
screen.title("Pixel Art")
turtle1 = turtle.Turtle()
turtle1.speed(1)

screen.colormode(255)
R=255
G=182
B=193
screen.bgcolor((R,G,B))

turtle.begin_fill()
turtle1.color("blue")

for i in range(6):
    turtle1.forward(100)
    turtle1.right(60)
turtle1.end_fill()
screen.mainloop()

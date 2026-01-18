import turtle
import random

screen=turtle.Screen()
screen.setup(800,800)
screen.bgcolor("white")

t=turtle.Turtle()
t.speed(0)
t.hideturtle()


def draw_rhombus(x, y, side, angle, rotation, color):
    t.penup()
    t.goto(x,y)
    t.setheading(rotation)
    t.pendown()

    t.fillcolor(color)
    t.begin_fill()

    for j in range(2):
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.left(180-angle)

    t.end_fill()
    t.penup()

for k in range(50):
    x = random.uniform(-300,300)
    y = random.uniform(-300,300)
    side = random.uniform(40,120)
    angle = random.uniform(30,150)
    rotation = random.uniform(0,360)
    color = (random.random(), random.random(), random.random())

    draw_rhombus(x,y,side,angle,rotation,color)


turtle.done()
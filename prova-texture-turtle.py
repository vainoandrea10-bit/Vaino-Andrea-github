import turtle
import random


screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Pixel Art")
t = turtle.Turtle()
t.speed(0.5)


def quadrato(lato, colore):
    t.fillcolor(colore)
    t.begin_fill()
    for i in range(4):
        t.forward(lato)
        t.right(90)
    t.end_fill()


lato = 50
righe = 8
colonne = 8
colori = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "cyan", "magenta", "lime", "black", "beige", "gold", "silver"]


t.penup()
t.goto(-200, 200)
t.pendown()


for r in range(righe):
    for c in range(colonne):
        quadrato(lato, random.choice(colori))
        t.forward(lato)

    
    t.penup()
    t.backward(lato * colonne)
    t.right(90) #la turtle deve girarsi di verso per andare giù 
    t.forward(lato) #va avanti di lato
    t.left(90) #si gira di nuovo verso destra
    t.pendown()

screen.mainloop()
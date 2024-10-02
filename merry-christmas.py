from turtle import *
from random import randint


def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.setheading(0)


def create_circle(turtle, x, y, radius, color):
    turtle2.penup()
    turtle2.color(color)
    turtle2.fillcolor(color)
    turtle2.goto(x, y)
    turtle2.pendown()
    turtle2.begin_fill()
    turtle2.circle(radius)
    turtle2.end_fill()


BG_COLOR = "#0080ff"

turtle2 = Turtle()
turtle2.speed(2)
screen = turtle2.getscreen()
screen.bgcolor(BG_COLOR)
screen.title("Feliz Natal")
y = -100
create_rectangle(turtle2, "red", -15, y - 60, 30, 60)
width = 240
turtle2.speed(10)

while width > 10:
    width = width - 10
    height = 10
    x = 0 - width / 2
    create_rectangle(turtle2, "green", x, y, width, height)
    y = y + height

turtle2.speed(1)
turtle2.penup()
turtle2.color("yellow")
turtle2.goto(-20, y + 10)
turtle2.begin_fill()
turtle2.pendown()

for i in range(5):
    turtle2.forward(40)
    turtle2.right(144)

turtle2.end_fill()
tree_height = y + 40

create_circle(turtle2, 230, 180, 60, "white")
create_circle(turtle2, 220, 180, 60, BG_COLOR)

turtle2.speed(10)
number_of_stars = randint(20, 30)

for _ in range(0, number_of_stars):
    x_star = randint(-(screen.window_width() // 2), screen.window_width() // 2)
    y_star = randint(tree_height, screen.window_height() // 2)
    size = randint(5, 20)
    turtle2.penup()
    turtle2.color("white")
    turtle2.goto(x_star, y_star)
    turtle2.begin_fill()
    turtle2.pendown()
    for i in range(5):
        turtle2.forward(size)
        turtle2.right(144)
    turtle2.end_fill()

turtle2.speed(1)
turtle2.penup()
msg = "Feliz Natal!"
turtle2.goto(0, -200)
turtle2.color("white")
turtle2.pendown()
turtle2.write(msg, move=False, align="center", font=("Arial", 15, "bold"))
turtle2.penup()
msg2 = "Abraços da equipe da Asimov!"
turtle2.goto(0, -230)
turtle2.color("white")
turtle2.pendown()
turtle2.write(msg2, move=False, align="center", font=("Arial", 15))

turtle2.hideturtle()
screen.mainloop()

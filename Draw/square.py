__author__ = 'Suraj'

import turtle

def draw_square(soms):
    soms.shape("turtle")
    soms.color("blue")

    for i in range(4):
        soms.forward(100)
        soms.right(90)

def draw_circle():
    soms = turtle.Turtle()
    soms.shape("turtle")
    soms.color("blue")
    soms.circle(100)


def draw_triangle():
    soms = turtle.Turtle()
    soms.shape("turtle")
    soms.color("blue")
    for i in range(3):
        soms.forward(100)
        soms.right(120)

def draw_diamond(soms):
    soms.shape("turtle")
    soms.color("blue")
    soms.forward(100)
    soms.right(135)
    soms.forward(100)
    soms.right(45)
    soms.forward(100)
    soms.right(135)
    soms.forward(100)
    soms.right(45)

window = turtle.Screen()
window.bgcolor("red")
soms = turtle.Turtle()
for i in range(36):
    draw_diamond(soms)
    soms.right(10)

soms.right(90)
soms.forward(500)
#draw_circle()
#draw_triangle()
window.exitonclick()
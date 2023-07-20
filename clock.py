from turtle import *

import turtle
import datetime

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Analog Clock")
screen.tracer(0)

# Create the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s):
    # Draw the clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(210)

    # Draw the hour marks
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # Draw the hour hand
    pen.up()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (h / 12) * 360 + (m / 60) * 30
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # Draw the minute hand
    pen.up()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (m / 60) * 360 + (s / 60) * 6
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

    # Draw the second hand
    pen.up()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

    # Display the current time
    pen.up()
    pen.goto(0, -250)
    pen.color("white")
    pen.write(datetime.datetime.now().strftime("%H:%M:%S"), align="center", font=("Courier", 24, "normal"))

    screen.update()

while True:
    h = datetime.datetime.now().hour
    m = datetime.datetime.now().minute
    s = datetime.datetime.now().second
    draw_clock(h, m, s)
    pen.clear()
# 
# ELEC7023
# Author: Zian Fang
# SID: 3036457584
#
# Assignment_1

from turtle import *

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
heart = turtle.Turtle()
heart.shape("arrow")
heart.color("blue")
heart.penup()
heart.goto(0,-100)
heart.pendown()
heart.speed(100)

# Draw the heart shape
heart.begin_fill()
heart.fillcolor("red")
heart.left(140)
heart.speed(10)
heart.forward(224)

for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.forward(224)
heart.end_fill()
heart.hideturtle()

# Close the turtle graphics window on click
turtle.exitonclick()
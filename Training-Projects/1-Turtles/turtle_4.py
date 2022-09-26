from time import sleep
from turtle import Turtle, Screen
import random

def spirograph(nr_circles):
    for i in range(nr_circles):
        change_color()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 5)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)

timmy = Turtle()
timmy.speed("fastest")
my_screen = Screen()

spirograph(200)

my_screen.exitonclick()
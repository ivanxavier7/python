from time import sleep
from turtle import Turtle, Screen
import random

def randow_walk(nr_paths):
    if nr_paths < 1:
        return "Please enter number of paths equal to or greater than one!"
    rand_paths = [0, 90, 180, 270]
    for i in range(nr_paths):
        change_color()
        timmy.left(random.choice(rand_paths))
        timmy.forward(30)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)

timmy = Turtle()
timmy.width(10)
timmy.speed(9)
my_screen = Screen()

randow_walk(500)

my_screen.exitonclick()
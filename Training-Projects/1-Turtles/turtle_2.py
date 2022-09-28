from turtle import Turtle, Screen
import random

def draw_shape(nr_sides):
    if nr_sides < 3:
        return "Please enter number of sides equal to or greater than three!"
    for i in range(3, nr_sides + 1):
        change_color()
        for j in range(i):
            timmy.forward(100)
            timmy.left(360 / i)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)

timmy = Turtle()
my_screen = Screen()

draw_shape(12)

my_screen.exitonclick()
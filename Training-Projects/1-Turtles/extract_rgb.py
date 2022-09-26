from time import sleep
from turtle import Turtle, Screen
import colorgram

def extract_colors(nr_colors):
    colors = colorgram.extract('C:\\course\\python\\Training-Projects\\1-Turtles\\teste.jpg', nr_colors)
    #for i in range(nr_colors):
    #    print("Cor número " + str(i) + ": ")
    #    print(colors[i])
    return colors

colors = extract_colors(10)

timmy = Turtle()
my_screen = Screen()
my_screen.colormode(255)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    timmy.pencolor(r, g, b)
    timmy.width(50)
    timmy.forward(50)

my_screen.exitonclick()
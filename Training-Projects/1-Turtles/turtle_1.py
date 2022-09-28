from turtle import Turtle, Screen

timmy = Turtle()
butters = Turtle()

my_screen = Screen()
print(my_screen.canvheight)

timmy.shape('turtle')
timmy.color('DarkGreen')

for i in range(4):
    timmy.forward(40)
    timmy.penup()
    timmy.forward(20)
    timmy.pendown()
    timmy.forward(40)
    timmy.left(90)

my_screen.exitonclick()
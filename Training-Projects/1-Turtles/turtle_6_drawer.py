from tkinter import W
from turtle import Turtle, Screen
import random
from pynput.keyboard import Key, Controller

class EtchASketch:

    def __init__(self) -> None:
        self.turtle = Turtle()
        self.screen = Screen()
        self.config_turtle()

    def move_forward(self):
        self.turtle.forward(10)

    def move_backward(self):
        self.turtle.backward(10)

    def move_left(self):
        self.turtle.setheading(self.turtle.heading() + 10)

    def move_right(self):
        self.turtle.setheading(self.turtle.heading() - 10)

    def assign_events(self):
        self.screen.listen()     
        self.screen.onkey(key="w", fun=self.move_forward)
        self.screen.onkey(key="s", fun=self.move_backward)
        self.screen.onkey(key="a", fun=self.move_left)
        self.screen.onkey(key="d", fun=self.move_right)
        self.screen.onkey(key="c", fun=self.clear)
        self.screen.onkey(key="k", fun=self.simulate_keyboard_circle)
        self.screen.exitonclick()

    def config_turtle(self):
        self.turtle.speed("fastest")
        self.turtle.width(5)
    
    def clear(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.home()
        self.turtle.pendown()
    
    def simulate_keyboard_circle(self):
        keyboard = Controller()
        for i in range(18):
            keyboard.press('w')
            keyboard.release('w')
            for j in range(2):
                keyboard.press('a')
                keyboard.release('a')


def main():
    drawer = EtchASketch()
    drawer.assign_events()

if __name__ == "__main__":
    main()
from tkinter import W
from turtle import Turtle, Screen
import random
from pynput.keyboard import Key, Controller

class TurtleRace:

    def __init__(self) -> None:
        self.screen = Screen()
        self.bet = ""
        self.turtles = []
        self.config_turtle()
        self.config_screen()    

    def config_turtle(self: Turtle):
        turtles_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        turtles_y_position = [-70, -40, -10, 20, 50, 80]
        for i in range(len(turtles_colors)):
            self.turtle = Turtle(shape="turtle")
            self.turtle.penup()
            self.turtle.speed(0)
            self.turtle.color(turtles_colors[i])
            self.turtle.goto(x=-230, y=turtles_y_position[i])
            self.turtles.append(self.turtle)
    
    def config_screen(self):
        self.screen.setup(width=500, height=400)
        self.bet = self.screen.textinput(title='Corrida de Tartarugas', prompt='Bet in one of the turtles: Red, Orange, Yellow, Green, Blue or Purple')
    
    def start(self):
        for turtle in self.turtles:
            if turtle.xcor() > 230:  # Verifica se ganha
                winning_color = turtle.pencolor()
                if winning_color == self.bet:
                    print(f"You've Won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've Lose! The {winning_color} turtle is the winner!")
                return False
            rand_distance = random.randint(0,10)
            turtle.forward(rand_distance)
        return True

def main():
    race = TurtleRace()
    race.bet = race.bet.lower()
    if race.bet == 'red' or race.bet == 'orange' or race.bet == 'yellow' or race.bet == 'green' or race.bet == 'purple':
        is_race_on = True
    
    while is_race_on:
        is_race_on = race.start()

    race.screen.exitonclick()

if __name__ == "__main__":
    main()
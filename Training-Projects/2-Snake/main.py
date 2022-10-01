from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SNAKE_DELAY = 0.1

screen = Screen()
screen.setup(width=1600, height=900)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(SNAKE_DELAY)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        # Increase Speed
        if SNAKE_DELAY > 0.01:
            SNAKE_DELAY -= 0.005
    
    # Detect collision with wall
    if snake.head.xcor() > 800 or snake.head.xcor() < -800 or snake.head.ycor() > 450 or snake.head.ycor() < -450:
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
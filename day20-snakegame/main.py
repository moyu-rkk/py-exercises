from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.show_score()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.update_score()

    # Detect collision with wall.
    if snake.head.xcor() < -300 or snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for seg in snake.snake_body[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

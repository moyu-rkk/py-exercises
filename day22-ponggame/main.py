from turtle import Screen
from board import Board
from racket import Racket
from ball import Ball
import time

# Screen set up.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# Ground and scoreboard set up.
scoreboard = Board()

scoreboard.draw_line()

# Generate rackets.
player_pos = (-350, 0)
computer_pos = (350, 0)

l_racket = Racket(player_pos)
r_racket = Racket(computer_pos)

screen.listen()
screen.onkey(l_racket.move_racket_up, "Up")
screen.onkey(l_racket.move_racket_down, "Down")
screen.onkey(r_racket.move_racket_up, "w")
screen.onkey(r_racket.move_racket_down, "s")

# Generate ball.
ball = Ball()

is_game_on = True
# within_upper_border = True
# within_bottom_border = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()

    # # computer racket movement
    # while within_upper_border:
    #     computer_racket.move_racket_up()
    #     if computer_racket.ycor() > 250:
    #         within_upper_border = False
    #         within_bottom_border = True
    #
    # while within_bottom_border:
    #     computer_racket.move_racket_down()
    #     if computer_racket.ycor() < -250:
    #         within_bottom_border = False
    #         within_upper_border = True

    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (l_racket.distance(ball) < 50 and ball.xcor() < -320) or (r_racket.distance(ball) < 50 and ball.xcor() > 320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

screen.exitonclick()

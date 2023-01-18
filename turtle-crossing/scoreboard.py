from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.goto(-270, 250)
        self.write(f"level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

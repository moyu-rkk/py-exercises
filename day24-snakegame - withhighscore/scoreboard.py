from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)

    def show_score(self):
        self.clear()
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

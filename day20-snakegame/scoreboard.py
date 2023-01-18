from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

with open("record.txt", "r") as file:
    RECORD = file.read()
file.close()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(RECORD)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)

    def show_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("record.txt", "w") as update_record:
                update_record.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

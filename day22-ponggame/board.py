from turtle import Turtle

FONT = ("Courier", 80, "normal")
ALIGNMENT = "center"


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def draw_line(self):
        self.goto(0, -300)
        self.setheading(90)
        self.color("white")
        self.pensize(5)
        for _ in range(20):
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

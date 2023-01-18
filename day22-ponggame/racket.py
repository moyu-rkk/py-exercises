from turtle import Turtle


MOVE_DISTANCE = 20


class Racket(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5.0, 1.0)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_racket_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_racket_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

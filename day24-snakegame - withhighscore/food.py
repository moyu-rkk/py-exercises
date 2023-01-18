from turtle import Turtle
import random

RANGE_START = -280
RANGE_END = 280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(RANGE_START, RANGE_END)
        random_y = random.randint(RANGE_START, RANGE_END)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(RANGE_START, RANGE_END)
        random_y = random.randint(RANGE_START, RANGE_END)
        self.goto(random_x, random_y)

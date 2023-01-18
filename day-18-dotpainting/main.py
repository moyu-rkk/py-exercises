import random
import colorgram
from turtle import Turtle, Screen

color_types = 7

color_source = colorgram.extract("kirby.jpg", color_types)

colors = []

for i in range(color_types):
    rgb_code = color_source[i].rgb
    red = rgb_code.r
    green = rgb_code.g
    blue = rgb_code.b
    colors.append((red, green, blue))

dave = Turtle()
dave.speed("fastest")

screen = Screen()
screen.colormode(255)

dots_size = 20
dots_per_line = 10
dots_interval = 50

x = -200
y = -200

dave.hideturtle()
dave.up()
dave.setx(x)
dave.sety(y)
dave.pd()
dave.showturtle()


def draw_dots(size, num, interval):
    for step in range(num):
        dave.dot(size, random.choice(colors))
        dave.up()
        dave.forward(interval)
        dave.pd()


for line in range(dots_per_line):
    draw_dots(dots_size, dots_per_line, dots_interval)
    y += dots_interval
    dave.up()
    dave.hideturtle()
    dave.setposition((x, y))
    dave.pd()
    dave.showturtle()


screen.exitonclick()


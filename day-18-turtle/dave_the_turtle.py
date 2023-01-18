from turtle import Turtle, Screen
import random

colors = ("#6CABDD", "#1C2C5B", "#FFC659", "#D4A12A", "#EC3325")

dave = Turtle()


dave.shape("triangle")

# 1. draw dashed line
# for _ in range(15):
#     dave.forward(10)
#     dave.up()
#     dave.forward(10)
#     dave.pd()


# 2. draw nested polygons with same side length
# def draw_polygon(animal, sides):
#     animal.color(random.choice(colors))
#     angle = 360/sides
#     for _ in range(sides):
#         animal.forward(100)
#         animal.right(angle)
#
#
# for shapes_n in range(3, 11):
#     draw_polygon(dave, shapes_n)

# 3. draw polygons with same radius
# def draw_poly_c(sides):
#     dave.circle(72, 360, sides)
#
#
# for i in range(3, 10):
#     dave.color(random.choice(colors))
#     draw_poly_c(i)


# 4. generate randoms walk with different color paths
#
screen = Screen()
screen.colormode(255)
# looks like the screen has default color mode to 1
# in which the rgb number tuple as color value evokes bad color sequence
#
# directions = [0, 90, 180, 270]
# dave.pensize(7)
dave.speed("fastest")
#
#
# def generate_move(step):
#     dave.seth(random.choice(directions))
#     dave.forward(step)


def generate_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color
#
#
# for _ in range(200):
#     dave.color(generate_color())
#     generate_move(27)
#
# screen.exitonclick()


def generate_circle():
    dave.color(generate_color())
    dave.circle(100, 360)


for angle in range(0, 360, 5):
    dave.setheading(angle)
    generate_circle()


screen.exitonclick()


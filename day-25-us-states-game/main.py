import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Customize screen shape by inserting a background image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

t = turtle.Turtle()
t.hideturtle()


def show_state(text, pos_x, pos_y):
    t.penup()
    t.goto(pos_x, pos_y)
    t.write(text)


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        x = data[data.state == answer_state].x
        y = data[data.state == answer_state].y

        show_state(answer_state, int(x), int(y))



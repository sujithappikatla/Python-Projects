import turtle
import pandas

win = turtle.Screen()
win.title("US States Game")
win.setup(width=800, height=600)
image = "blank_states_img.gif"
win.addshape(image)
turtle.shape(image)

us_states_data = pandas.read_csv("50_states.csv")
data_states = us_states_data["state"].to_list()
guessed_states = []
while len(guessed_states) != 50:
    state = win.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another"
                                                                                   " state's name?").title()
    if state == "Exit":
        missed_states = []
        for s in data_states:
            if s not in guessed_states:
                missed_states.append(s)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if state in data_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        current_state_data = us_states_data[us_states_data.state == state]
        t.goto(int(current_state_data.x), int(current_state_data.y))
        t.write(current_state_data.state.item(), align="center")
        guessed_states.append(state)

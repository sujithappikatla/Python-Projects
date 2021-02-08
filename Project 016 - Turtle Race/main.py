from turtle import Turtle, Screen
import random

win = Screen()
win.setup(width=500, height=400)
user_choice = win.textinput("Make your bet", "Which turtle will win the Race? Enter a color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

start_y = -100
for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=-230, y=start_y)
    start_y += 40
    turtles.append(tim)

is_race_on = True
winner = ""
while is_race_on:
    for tim in turtles:
        rand_distance = random.randint(0, 10)
        tim.forward(rand_distance)
        if tim.xcor() >= 230:
            is_race_on = False
            (_, winner) = tim.color()
            break

if winner == user_choice:
    print(f"You Win!!, Winner is {winner}")
else:
    print(f"You Lose...  Winner is {winner}")

win.exitonclick()

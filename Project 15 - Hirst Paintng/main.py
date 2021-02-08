from turtle import Turtle, Screen
import random
import colorgram as cg

rgb_colors = []
colors = cg.extract("image.jpg", 50)
for color in colors:
    (r, g, b) = color.rgb
    rgb_colors.append((r, g, b))

tim = Turtle()
win = Screen()
win.colormode(255)
win.title("Hirst Dot Painting")
win.bgcolor((0, 0, 0))
tim.shape('arrow')
tim.penup()
tim.hideturtle()
tim.setposition(0, 220)
tim.color("white")
tim.write("Hirst Dot Painting", True, "center", ("Arial", 15, "bold"))
tim.setposition(-200, -200)
tim.speed("fastest")


for __ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(40)
    current_y = tim.pos()[1]
    tim.sety(current_y + 40)
    tim.setx(-200)


win.exitonclick()

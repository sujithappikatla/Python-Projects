from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Window Creation
win = Screen()
win.setup(width=600, height=600)
win.bgcolor('black')
win.title("Snake Game")
win.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()

# Window Keybindings
win.listen()
win.onkey(snake.up, "Up")
win.onkey(snake.down, "Down")
win.onkey(snake.left, "Left")
win.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    win.update()
    time.sleep(0.1)
    snake.move()

    # if snake touch food then refresh food and increase score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # if snake touches any four sides of wall then game over
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    # If snake collides with its own body then game over
    if snake.check_for_collision():
        score.reset()
        snake.reset()

win.exitonclick()

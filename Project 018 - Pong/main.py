from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

win = Screen()
win.bgcolor('black')
win.setup(width=800, height=600)
win.title("Pong Game")
win.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = ScoreBoard()

win.listen()
win.onkeypress(r_paddle.go_up, "Up")
win.onkeypress(r_paddle.go_down, "Down")

win.onkeypress(l_paddle.go_up, "w")
win.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    win.update()

    ball.move()

    if ball.xcor() > 390:
        score.l_point()
        ball.reset()
    if ball.xcor() < -390:
        score.r_point()
        ball.reset()

    if l_paddle.ycor()+50 > ball.ycor() > l_paddle.ycor()-50 and -360 < ball.xcor() < -330:
        ball.move_speed *= 0.9
        ball.setx(-330)
        ball.dx *= -1
    if r_paddle.ycor()+50 > ball.ycor() > r_paddle.ycor()-50 and 360 > ball.xcor() > 330:
        ball.move_speed *= 0.9
        ball.setx(330)
        ball.dx *= -1

win.exitonclick()

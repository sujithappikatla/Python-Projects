from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.speed("fastest")
        self.home()
        self.dx = 5
        self.dy = 5
        self.move_speed = 0.05

    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)
        if self.ycor() > 290 or self.ycor() < -290:
            self.dy *= -1

    def reset(self):
        self.home()
        self.dx *= -1
        self.move_speed = 0.05

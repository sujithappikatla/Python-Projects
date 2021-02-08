from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_cor, y_cor)
        self.color('white')
        self.penup()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

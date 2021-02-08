from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        """Moves player when up arrow key pressed"""
        self.forward(10)

    def reset(self):
        """After reaching finish line get back to starting position"""
        self.setposition(STARTING_POSITION)

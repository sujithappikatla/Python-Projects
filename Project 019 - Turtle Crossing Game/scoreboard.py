from turtle import Turtle
FONT = ("Courier", 18, "normal")
GAME_OVER_FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition((-270, 260))
        self.score = 0
        self.write(f"Score : {self.score}", False, "left", FONT)

    def update_score(self):
        """Update Score on every successful finish line reached"""
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", False, "left", FONT)

    def game_over(self):
        """Write game Over """
        self.home()
        self.write("Game Over", False, "center", GAME_OVER_FONT)

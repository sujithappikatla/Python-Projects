from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        with open("high_score.txt", "r") as hs:
            self.high_score = int(hs.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as hs:
                hs.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        # self.home()
        # self.write("Game Over", False, ALIGNMENT, FONT)

    def increase_score(self):

        self.score += 1
        self.update_scoreboard()

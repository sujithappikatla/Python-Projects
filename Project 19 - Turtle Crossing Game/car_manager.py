from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_POSITION = 290
MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.cars = []

    def create_cars(self):
        """Create cars randomly"""
        num_of_cars = random.randint(0, 3)
        for _ in range(num_of_cars):
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.penup()
            car.setposition((STARTING_POSITION, random.randrange(-220, 250, 40)))
            self.cars.append(car)

    def move_cars(self):
        """Move all cars by certain speed"""
        for car in self.cars:
            car.forward(MOVE_DISTANCE)
            if car.xcor() < -320:
                self.cars.pop(self.cars.index(car))

    def collision(self, player):
        """Check for Collision with player """
        for car in self.cars:
            if player.distance(car) <= 30 and car.ycor()-10 <= player.ycor() <= car.ycor()+10:
                return True
        return False

    def increase_speed(self):
        """Increase speed of cars movement"""
        global MOVE_DISTANCE
        MOVE_DISTANCE += 3

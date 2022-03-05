import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.5


class CarManager:

    def __init__(self):
        self.car = None
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            self.car = Turtle()
            self.car.shape("square")
            self.car.penup()
            self.car.shapesize(stretch_len=2)
            self.car.color(random.choice(COLORS))
            self.car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(self.car)

    def car_mover(self):
        for car in self.all_cars:
            car.back(self.move_speed)

    def level_up(self):
        self.move_speed *= MOVE_INCREMENT



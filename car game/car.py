from turtle import Turtle
COLORS=["red","green","orange","yellow","black","purple","blue","pink"]
STARTING_MOV_DISTANCE=5
MOV_INCREMENT=10
import random
class Car:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOV_DISTANCE

    def create(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-230,230)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOV_INCREMENT

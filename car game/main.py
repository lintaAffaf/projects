from turtle import Screen, Turtle
from timmy import Timmy
from car import Car
from score import Score
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
t = Timmy()
car = Car()
score=Score()

screen.listen()
screen.onkeypress(t.move_up, "Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    car.create()
    car.move()
    # detect collision with car
    for cars in car.all_cars:
        if cars.distance(t) < 20:
            score.game_over()
            game_on = False

    # detect collision with edge
    if t.is_at_finishline():
        t.reset_turtle()
        car.increase_speed()
        score.increase_level()


screen.exitonclick()




















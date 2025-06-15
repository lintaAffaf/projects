from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Score()


# Track key states
keys_held = {
    "Up": False,
    "Down": False,
    "w": False,
    "s": False
}

# Press and release handlers
def press_key(key):
    keys_held[key] = True

def release_key(key):
    keys_held[key] = False

screen.listen()
screen.onkeypress(lambda: press_key("w"), "w")
screen.onkeypress(lambda: press_key("s"), "s")
screen.onkeypress(lambda: press_key("Up"), "Up")
screen.onkeypress(lambda: press_key("Down"), "Down")

screen.onkeyrelease(lambda: release_key("w"), "w")
screen.onkeyrelease(lambda: release_key("s"), "s")
screen.onkeyrelease(lambda: release_key("Up"), "Up")
screen.onkeyrelease(lambda: release_key("Down"), "Down")

def move_paddles():
    if keys_held["w"]:
        l_paddle.move_up()
    if keys_held["s"]:
        l_paddle.move_down()
    if keys_held["Up"]:
        r_paddle.move_up()
    if keys_held["Down"]:
        r_paddle.move_down()

game_on=True
while game_on:
    screen.update()
    move_paddles()
    time.sleep(ball.movespeed)
    ball.move()
    #detect collision with wall
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()
    #detect collision with  paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    #right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.score_increaseleft()
    #left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.score_increaseright()



screen.listen()
screen.exitonclick()

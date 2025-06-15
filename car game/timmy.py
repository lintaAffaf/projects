from turtle import Turtle
STARTING_POSITIONS=(0,-280)
MOV_DISTANCE=10
FINISH_LINE_Y=280

class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITIONS)

    def move_up(self):
        self.forward(MOV_DISTANCE)

    def reset_turtle(self):
            self.goto(STARTING_POSITIONS)

    def is_at_finishline(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False






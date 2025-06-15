from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.leftscore=0
        self.rightscore=0
        self.goto(0,250)
        self.write(f"{self.leftscore} : {self.rightscore}", move=False, align="center", font=("Arial", 20, "normal"))

    def score_increaseright(self):
        self.rightscore+=1
        self.clear()
        self.refresh()

    def score_increaseleft(self):
        self.leftscore += 1
        self.clear()
        self.refresh()

    def refresh(self):
        self.write(f"{self.leftscore} : {self.rightscore}", move=False, align="center",
                   font=("Arial", 20, "normal"))





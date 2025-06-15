from turtle import Turtle
FONT=("Arial", 20, "normal")
LEVEL=1
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-290,270)
        self.refresh()


    def increase_level(self):
        self.level +=1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="left", font=(FONT))

    def game_over(self):
        self.goto(0,0)
        self.write("GAMEOVER", move=False, align="CENTER", font=(FONT))

















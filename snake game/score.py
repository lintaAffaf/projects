from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore =int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score:{self.score} high score:{self.highscore}", move=False, align='center', font=('Arial', 15, 'normal'))

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"self.highscore")
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()












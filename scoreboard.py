from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-20, 270)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f" OOPS ! Game Over" ,align="center",font=("Arial", 30, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="left", font=("Arial", 15, "normal"))

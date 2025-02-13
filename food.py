from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        x_ran=random.randint(-280,280)
        y_ran=random.randint(-280,280)
        self.goto(x_ran,y_ran)
    def refresh(self):
        x_ran = random.randint(-280, 280)
        y_ran = random.randint(-280, 280)
        self.goto(x_ran, y_ran)

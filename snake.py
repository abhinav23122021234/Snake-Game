from turtle import Screen,Turtle
import time
screen=Screen()
DOWN=270
LEFT=180
UP=90
RIGHT=0
class Snake:
    def __init__(self):
        self.snake_body=[]
        self.create_snake()
        self.head=self.snake_body[0]

    def create_snake(self):
        # TODO 1 : Create Snake body : 3 Square turtles lined up adjacent to each other
        x = 0
        y = 0
        for i in range(0, 3):
            snake_part = Turtle("square")
            snake_part.color("white")
            self.snake_body.append(snake_part)
            snake_part.penup()
            snake_part.goto(x, y)
            x -= 20
        self.snake_body[0].color("green")
    # TODO 2 : Make the snake move
    def move_snake(self):
        screen.tracer(0)
        for i in range(len(self.snake_body) - 1, 0, -1):
            x_new = self.snake_body[i - 1].xcor()
            y_new = self.snake_body[i - 1].ycor()
            self.snake_body[i].speed("fastest")
            self.snake_body[i].goto(x_new, y_new)
        self.snake_body[0].forward(20)
        time.sleep(0.1)
        screen.update()


    def extend(self):
        snake_part = Turtle("square")
        snake_part.color("white")
        self.snake_body.append(snake_part)
        snake_part.penup()
        x_cor=self.snake_body[len(self.snake_body)-2].xcor()
        y_cor=self.snake_body[len(self.snake_body)-2].ycor()
        self.snake_body[len(self.snake_body)-1].goto(x_cor,y_cor )


    # TODO 3 : control snake head using keys
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head=self.snake_body[0]

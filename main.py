from turtle import Turtle,Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard
scores=Scoreboard()
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake=Snake()
food=Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:

    snake.move_snake()
    screen.update()
    time.sleep(0.1)

    if food.distance(snake.head)<15:
        food.refresh()
        scores.increase_score()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 :
        game_is_on=False
        scores.game_over()

    #Detect collision with tail
    for segment in snake.snake_body[1::-1]:
        if snake.head.distance(segment)<10:
            scores.game_over()
            game_is_on=False

screen.exitonclick()

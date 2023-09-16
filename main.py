from turtle import Screen
from scoreboard import ScoreBoard
from food import Food
from snake import Snake
import time


sc = Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)

snake = Snake()
foo = Food()
score = ScoreBoard()

sc.listen() 
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    
    snake.move()
    
    if snake.head.distance(foo) < 14:
        foo.refresh()
        snake.extend()
        score.inc_score()

    if snake.head.xcor() < -280 or snake.head.xcor()>280 or snake.head.ycor()< -280 or snake.head.ycor()>280:
        # score.game_over()
        # game_is_on=False    
        score.score_reset()
        snake.snake_reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score.game_over()
            score.score_reset()
            snake.snake_reset()
sc.exitonclick()
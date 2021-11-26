from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


def stop_playing():
    global game_is_on
    game_is_on = False
    exit()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(stop_playing, 's')

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()



    # Detect collision with food.
    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.restart()
        snake.restart()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.restart()
            snake.restart()






















screen.exitonclick()

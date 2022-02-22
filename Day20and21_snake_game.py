from turtle import Screen
from Day20and21_snake_move_class import Snake
from Day20and21_snake_scoreboard_class import Scoreboard
from Day20and21_snake_food_class import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)


game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

scoreboard.update_score()

screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food.xcor(), food.ycor()) < 10:
        food.refresh()
        scoreboard.update_score()
        snake.add_segment()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290:
        game_is_on = False
    if snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False

scoreboard.game_over()

screen.exitonclick()

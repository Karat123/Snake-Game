from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.snake_left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

     # Detecting collisions of snake with food
    if snake.snake_segments[0].distance(food) <= 20:
        food.refresh()
        scoreboard.update_score()
        snake.snake_extend()

    # Detecting collisions of snake with walls
    if snake.snake_segments[0].xcor() > 280 or snake.snake_segments[0].xcor() < -280 or snake.snake_segments[0].ycor() > 280 \
            or snake.snake_segments[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()





    # Detecting collisions of snake with itself
    for i in snake.snake_segments[1:]:
        if snake.snake_segments[0].distance(i) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()













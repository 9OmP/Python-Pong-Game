import time
from turtle import Turtle, Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_b = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collisions with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collisions with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.reflect()

    # Detect misses with r_paddle
    if ball.xcor() > 380:
        ball.go_back()
        l_paddle.go_back((-350, 0))
        r_paddle.go_back((350, 0))
        score_b.l_point()
        score_b.update_scoreboard()

    # Detect misses with l_paddle
    if ball.xcor() < -380:
        ball.go_back()
        l_paddle.go_back((-350, 0))
        r_paddle.go_back((350, 0))
        score_b.r_point()
        score_b.update_scoreboard()

screen.exitonclick()

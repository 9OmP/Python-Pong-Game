import time
from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.y_move = 10
        self.x_move = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.move_speed = 0.01

    def move(self):
        time.sleep(0.1)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def reflect(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def go_back(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
        self.move_speed = 0.01


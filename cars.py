from turtle import Turtle
from random import choice


color = ['black', 'blue', 'red', 'green', 'yellow']


class cars(Turtle):
    def __init__(self, position):
        super().__init__()
        self.move_x = 10
        self.colors = choice(color)
        self.shape('square')
        self.color(self.colors)
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.penup()
        self.left(90)
        self.goto(position)
        self.time_sleep = 0.1
        
    def movement(self):
        new_x = self.xcor() - self.move_x
        self.goto(new_x, self.ycor())
        self.resetPos()

    def resetPos(self):
        if self.xcor() < - 380:
            self.goto(400, self.ycor())

    def increase_speed(self):
        self.time_sleep *= 0.05


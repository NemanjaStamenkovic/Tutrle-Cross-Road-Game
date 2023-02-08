from turtle import Turtle

class group_turtles(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.speed = 0
        self.left(90)
        self.goto(0, -260)
        self.shapesize(stretch_wid= 2, stretch_len= 2)

    def movement(self):
        self.speed = 20
        new_y = self.ycor() + self.speed
        self.goto(0, new_y)

    def resetTurtle(self):
        self.goto(0, -260)
        
        
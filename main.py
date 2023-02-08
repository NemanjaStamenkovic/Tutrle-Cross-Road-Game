from turtle import Screen
from turtles import group_turtles
from scoreboard import ScoreBoard
from cars import cars
import random
import time

#screen Setup
screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("orange")
screen.title("Turtle Cross Road")
screen.tracer(0)


#game objects
count = 0
cars_online = []
turtle = group_turtles()
score = ScoreBoard()


screen.listen()
screen.onkey(turtle.movement, "Up")


def spawnCars():
    global count
    random_y = random.randint(-200, 200)
    random_x = random.randint(-350, 350)
    car = cars((random_x, random_y))
    count += 1
    cars_online.append(car)    


game = True


while game:

    time.sleep(score.time_sleep)
    screen.update()
    

    if count < 15:
        spawnCars()


    for car in cars_online:
        car.movement()


    if turtle.ycor() > 280:
        score.increase_speed()
        turtle.resetTurtle()
        score.increase_score()


    for car in cars_online:
        if turtle.distance(car) < 40:
                game = False
else:
    screen.clear()
    score.game_over()

    
screen.exitonclick()
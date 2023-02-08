from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color = "black"
        self.hideturtle()
        self.penup()
        self.goto(-350, 260)
        self.update()
        self.time_sleep = 0.1

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def update(self):
        self.write(f"Level: {self.score}", font=("Arial", 16, "normal"))

    def increase_speed(self):
        self.time_sleep *= 0.12

    def game_over(self):
        self.goto(-230, 0)
        self.write("GAME OVER", font=("Arial", 60, "normal"))
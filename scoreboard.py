from turtle import Turtle

FONT = ("Ariel", 20, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.show_score()

    def show_score(self):
        self.write(f"Score : {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

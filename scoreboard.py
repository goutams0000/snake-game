from turtle import Turtle

FONT = ("Ariel", 20, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.show_score()

from turtle import Turtle
FONT=('Courier',20,'normal')

class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.lvl=1
        self.goto(0,270)
        self.update_lvl()

    def update_lvl(self):
        self.clear()
        self.write(f'Score: {self.lvl}', align='center',font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over', align='center',font=FONT)
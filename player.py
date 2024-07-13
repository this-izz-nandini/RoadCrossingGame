from turtle import Turtle
START_POS=(0,-270)
DIST=10
FINISH_LINE=280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.reset_pos()

    def move(self):
        self.fd(DIST)

    def reset_pos(self):
        self.goto(START_POS)
from turtle import Turtle, Screen
from player import Player
from cars import CarMgr
from scorecard import ScoreCard

import time, random

screen=Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

p=Player()

c=CarMgr()

s=ScoreCard()
game_on=True

while game_on:
    time.sleep(0.1)
    screen.update()

    c.create_car()
    c.move_cars()
    screen.onkeypress(p.move,'Up')

    for car in c.all_cars:
        if p.distance(car)<20:
            s.game_over()
            game_on=False
            
    if p.ycor() >= 250:
        p.reset_pos()
        c.lvl_up()
        s.lvl+=1
        s.update_lvl()

screen.exitonclick()
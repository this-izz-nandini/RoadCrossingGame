from turtle import Turtle
import random

COLORS=['lawn green','medium violet red','powder blue','light sea green','dark blue','orchid','red','orange','yellow','green','blue','purple']
INITIAL_SPEED=5
MOVE_INC=5

class CarMgr():
    def __init__(self):
        self.all_cars=[]
        self.car_reserve = [] 
        self.car_speed=INITIAL_SPEED    

    def create_car(self):
        freq=random.randint(1,5)
        if freq==1:
            if self.car_reserve:
                car = self.car_reserve.pop()
            else:
                car=Turtle('square')
                car.shapesize(stretch_wid=1,stretch_len=2)
                car.penup()
                car.color(random.choice(COLORS))
            car.goto(280,random.randrange(-240,240,20))
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.bk(self.car_speed)
            if car.xcor()<-320:
                self.all_cars.remove(car)
                self.car_reserve.append(car)

    def lvl_up(self):
        self.car_speed+=MOVE_INC

from contextlib import nullcontext
from turtle import Turtle
import random

#MOVE_DISTANCE = 5

#randomX = random.randint(-290,290)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        #self.speed('slowest')
        
    def move(self):
        #randomY = random.randint(-290,290)
        #self.goto(400, randomY)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1 
    
    def bounce_x(self):
        self.x_move *= -1 
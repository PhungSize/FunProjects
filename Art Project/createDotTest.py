from turtle import Turtle
import random

class Dot(Turtle):
    def __init__(self):
        super().__init__()
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.shapesize(.2,.2)
        self.penup()
        self.shape('circle')
        self.goto(x_pos, y_pos)
        self.stamp()
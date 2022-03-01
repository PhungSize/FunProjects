from turtle import Turtle, Shape, register_shape, shape
import random

COLORS = ["red", "orange", "gold", "green", "blue", "purple"]

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
        
class Line(Turtle):
    def __init__(self, point_list):
        super().__init__()
        point1 = random.choice(point_list)
        point2 = random.choice(point_list)
        while point1 == point2:
            point2 = random.choice(point_list)
        self.hideturtle()
        self.color(random.choice(COLORS))
        self.penup()
        self.setpos(point1.xcor(), point1.ycor())
        self.pendown()
        self.goto(point2.xcor(), point2.ycor())

class Triangle(Turtle):
    def __init__(self, point_list):
        super().__init__()
        point1 = random.choice(point_list)
        point2 = random.choice(point_list)
        point3 = random.choice(point_list)
        while point1 == point2:
            point2 = random.choice(point_list)
        while point1 == point3:
            point3 = random.choice(point_list)
        poly = (point1.xcor(), point1.ycor()),(point2.xcor(), point2.ycor()),(point3.xcor(), point3.ycor())
        # register_shape('triangle', poly)
        # self.shape('triangle')
        # self.stamp()
        
        s = Shape("compound")
        s.addcomponent(poly, random.choice(COLORS))
        register_shape("myshape", s)
        self.shape("myshape")
        self.stamp()
       
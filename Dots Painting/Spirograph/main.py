import turtle as t
from turtle import Screen
import random

# tim = t.Turtle()
# tim.speed(4)
# #tim.pensize(7)
# screen = Screen()
# #screen.exitonclick()


# #draws a polyhedral shape with X sides
# def drawShape(number):
#     red = random.randint(1,255)
#     blue = random.randint(1,255)
#     green = random.randint(1,255)
#     screen.colormode(255)
#     angle = 360/number
#     tim.pencolor(red, green, blue) 
#     for i in range(number):
#         tim.forward(100)
#         tim.right(angle)

# # for i in range(4,20):
# #     drawShape(i)

# def randomDirection():
#     direction = random.randint(0,3)
#     newDirection = direction * 90
#     tim.right(newDirection)

# def randomMovement():
#     red = random.randint(1,255)
#     blue = random.randint(1,255)
#     green = random.randint(1,255)
#     screen.colormode(255)
#     tim.pencolor(red, green, blue)
#     randomDirection()
#     tim.forward(50)
    
# def drawCircles():
#     red = random.randint(1,255)
#     blue = random.randint(1,255)
#     green = random.randint(1,255)
#     screen.colormode(255)
#     tim.pencolor(red, green, blue)

# def drawDots():
#     randomColor = random.choice(rgb_color)
#     print(randomColor)
#     screen.colormode(255)
#     tim.pencolor(randomColor)
#     tim.dot(size=20)

import turtle as t
import random

tim = t.Turtle()
tim.speed('fastest')
tim.hideturtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         print(tim.heading())
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)
    
t.colormode(255)
tim = t.Turtle()
tim.speed(10)

tim.pu()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.pd()

def changeRows():
    tim.pu()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    tim.pd()

rgb_colors = [(199, 12, 32), (250, 238, 16), (39, 76, 189), (238, 227, 5), (38, 217, 68), (229, 159, 46), (27, 39, 158), (215, 75, 12), (198, 14, 11), (15, 154, 15), (242, 246, 251), (243, 34, 166), (230, 17, 121), (70, 10, 31), (61, 15, 8), (225, 141, 210), (10, 98, 62), (224, 160, 7), (49, 213, 231), (17, 19, 44), (11, 227, 239), (237, 156, 220), (86, 74, 210), (77, 212, 165), (85, 233, 198), (56, 233, 242), (4, 68, 41)]

def drawDots():
    for x in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.pu()
        tim.fd(50)
        tim.pd()

for x in range(10):
    drawDots()
    changeRows()



screen = t.Screen()
screen.exitonclick()
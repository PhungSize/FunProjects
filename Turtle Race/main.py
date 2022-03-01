import turtle as t
from turtle import Screen, shape, textinput
import random


# Project Etch and Sketch vvvvvv

tim = t.Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.back(10)

def turn_left():
    tim.setheading(tim.heading() + 10)
    
def turn_right():
    tim.setheading(tim.heading() - 10)
    
def clear_screen():
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()

# Project Etch and Sketch ^^^^^^^^




# Project Race VVVVVVV

# is_race_on = False

# screen = Screen()
# screen.setup(width = 500, height = 400)
# user_answer = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# all_turtles = []
# y_axis = -100
# for turtle_index in range(0,6):
#     turtle = t.Turtle(shape="turtle")
#     turtle.color(colors[turtle_index])
#     turtle.penup()
#     turtle.goto(x= -230, y = y_axis)
#     y_axis += 50
#     all_turtles.append(turtle)
    
# if user_answer:
#     is_race_on = True
    
# while is_race_on == True:
#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             if user_answer == turtle.pencolor():
#                 print(f"You're right! The winner is {turtle.pencolor()}!")
#             else:
#                 print(f"You're wrong! The winner is {turtle.pencolor()}!")
#             is_race_on = False
#         rand_distance = random.randint(0,10)
#         turtle.forward(rand_distance)

# screen.exitonclick()


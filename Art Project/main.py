import tkinter as tk
from turtle import Screen
from createDot import Dot, Line, Triangle

top = tk.Tk()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.textinput("title", "prompt")

list_of_points = []
list_of_lines = []

for x in range(100):
    dot = Dot()
    list_of_points.append(dot)

for x in range(24):
    triange = Triangle(list_of_points)

for x in range(100):
    line = Line(list_of_points)
    list_of_lines.append(line)

screen.update()
    
screen.exitonclick()
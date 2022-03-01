import tkinter as tk
from turtle import TurtleScreen, RawTurtle, Turtle

def set_position():
    player.setposition(x_entry.get(), y_entry.get())
    player.dot(30, 'blue')
    player.home()

top = tk.Tk()

canvas = tk.Canvas(top, width=600, height=600)
canvas.pack()

screen = TurtleScreen(canvas)
screen.bgcolor('black')

player = Turtle(screen)
player.shape('turtle')
player.color('red', 'white')
player.penup()

# x_entry = tk.DoubleVar()
# tk.Label(top, text="X: ").pack(side=tk.LEFT)
# tk.Entry(top, textvariable=x_entry).pack(side=tk.LEFT)

# y_entry = tk.DoubleVar()
# tk.Label(top, text="Y: ").pack(side=tk.LEFT)
# tk.Entry(top, textvariable=y_entry).pack(side=tk.LEFT)

# tk.Button(top, text="Draw Dot!", command=set_position).pack()

screen.mainloop()
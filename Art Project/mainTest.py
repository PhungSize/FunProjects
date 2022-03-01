import tkinter as tk
from turtle import TurtleScreen
from createDotTest import Dot
top = tk.Tk()

canvas = tk.Canvas(top, width=600, height=600)
canvas.pack()

screen = TurtleScreen(canvas) 
screen.tracer(0)

dot = Entry(top)
dot.pack()
el = Entry(top)
el.pack()

list_of_points = []
list_of_lines = []

# for x in range(100):
#     dot = Dot()
#     list_of_points.append(dot)

# linesAns = Button(root,text='Lines',command=linesFunction)
# linesAns.pack(side='bottom')
# pointsAns = Button(root,text='Points',command=pointsFunction)
# pointsAns.pack(side='bottom')
# clearAns = Button(root,text='Clear',command=clearFunction)
# clearAns.pack(side='bottom')

screen.mainloop()
import random
from random import randrange
from tkinter import *

#making Main Window
root = Tk()
root.title("Reston Hackathon 2020")
canvas = Canvas(root, width=600, height=600)
root.resizable(False, False)
root.geometry("+350+250")
canvas.pack()


global x1, y1, xList, yList, slopeList, slope1, slope2, colors

colors = ["red", "orange", "yellow", "green", "blue", "violet"]

xList = []
yList = []
slopeList = []

#Functions
def pointsFunction():
	
	answer = dot.get() 
	intAnswer = int(answer)

	for x in range(0,intAnswer):
		x1 = randrange(500)
		y1 = randrange(500)
		canvas.create_oval(x1, y1, x1, y1, width = 1.5, fill = 'black')
		
		xList.append(x1)
		yList.append(y1)
		#print(xList)
		#print(yList)
		print("x=" + str(x1) + " y=" +str(y1) +"\n")

	
def linesFunction():

	answer = el.get()
	intAnswer = int(answer)
	
	for x in range(0, intAnswer):

		x2 = random.choice(xList)
		x3 = random.choice(xList)

		#This is to ensure that point 1 != point 2
		while x2 == x3:
			x2 = random.choice(xList)
		
		indexForY2 = xList.index(x2)
		indexForY3 = xList.index(x3)

		y2 = yList[indexForY2]
		y3 = yList[indexForY3]

		slope = ((y3-y2)/(x3-x2))

		#slopeList.append(slope)
		#print(slopeList)
		
		print("Slope is " + str(slope))
		print("x2=" +str(x2)+ " y2=" + str(y2) + " x3=" + str(x3) + " y3=" +str(y3))

		if slope not in slopeList and (x2 and x3 not in slopeList):
			canvas.create_line(x2, y2, x3, y3, fill="black")
			slopeList.append(slope)
		
		elif slope in slopeList:
			canvas.create_line(x2, y2, x3, y3, fill= random.choice(colors))


def clearFunction():
	canvas.delete("all")
	xList[:] = []
	yList[:] = []
	slopeList[:] = []	



#User Input for GUI
dot = Entry(root)
dot.pack()
el = Entry(root)
el.pack()
#perp = Entry(root)
#perp.pack()

#perpAns = Button(root,text='Perp',command=perpFunction)
#perpAns.pack(side='bottom')
linesAns = Button(root,text='Lines',command=linesFunction)
linesAns.pack(side='bottom')
pointsAns = Button(root,text='Points',command=pointsFunction)
pointsAns.pack(side='bottom')
clearAns = Button(root,text='Clear',command=clearFunction)
clearAns.pack(side='bottom')



root.mainloop()

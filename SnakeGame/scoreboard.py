from turtle import Turtle, Screen

ALIGN = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)
        
    def addScore(self): 
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font= FONT)
        
    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over.", move=False, align=ALIGN, font= FONT)
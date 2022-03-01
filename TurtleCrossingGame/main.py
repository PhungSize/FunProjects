import time
from turtle import Screen, exitonclick
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
car_manager = CarManager()
turtle = Player()
screen.onkey(turtle.forward, "w")
screen.onkey(turtle.backward, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    #Detect Collision
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            
    #Detect to reach other side
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        car_manager.level_up()
        
            
screen = exitonclick()

    

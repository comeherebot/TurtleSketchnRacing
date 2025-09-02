"""Turtle Racing Game"""
from turtle import *
import random
screen = Screen()
colors = ["red", "blue", "green", "purple", "violet"]
screen.setup(1000,700)
positions = [-200, -100, 0, 100, 200]
is_game_on= False
turtles= []
for i in range(5):
    tim= Turtle()
    tim.color(colors[i])
    tim.shape("turtle")
    tim.penup()
    tim.goto(x=-390,y=positions[i])
    tim.pendown()
    turtles.append(tim)
def finish_line():
    hideturtle()
    penup ( )
    goto (280, 210)
    pendown ( )
    setheading (heading ( ) + 270)
    pensize (4)
    pencolor ("green")
    fd (410)
finish_line()
user_bet = screen.textinput (title="Which color of turtle you choose?", prompt="red, blue, green, purple, violet.\nEnter Yours: ")
if user_bet:
    is_game_on= True

while is_game_on:
    for i in turtles:
        i.fd(random.randint(5,10))
        if i.xcor()> 280:
            is_game_on = False
            winner= i.pencolor()
            if winner==user_bet:
                print(f"Your {winner} turtle is won!!!")
            else:
                print (f"{winner} turtle is won!!! You lose")
exitonclick()
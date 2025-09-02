from turtle import *
tim= Turtle()
screen= Screen()
def left():

    backward (20)
def right():
    forward (20)
def up():
    new_heading= heading() + 20
    setheading(new_heading)
def down():
    new_heading = heading ( ) - 20
    setheading (new_heading)
def clear():
    clear()
    reset()


screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(reset, "r")
screen.listen()
screen.exitonclick()
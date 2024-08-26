from turtle import *
from random import *

def moveToRandomLocation():
    penup()
    setpos(randint(-400, 400),randint(-400, 400))
    pendown()

def drarStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()

    for side in range(5):
        left(144)
        forward(starSize)
        
    end_fill()
    penup()

bgcolor("MidnightBlue")

for star in range(30):
    moveToRandomLocation()
    drarStar(randint(5,25), 'White')

hideturtle()
done()
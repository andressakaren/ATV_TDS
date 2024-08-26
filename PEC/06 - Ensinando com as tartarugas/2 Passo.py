from turtle import *

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

drarStar(50, 'Red')
forward(100)
drarStar(30, 'White')
left(120)
forward(150)
drarStar(70, 'Green')

hideturtle()
done()
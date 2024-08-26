from turtle import *

def drawCirculo(radius, starColour):
    pendown()
    begin_fill()
    
    color(starColour)
    circle(radius)
    
    end_fill()
    penup()

bgcolor("MidnightBlue")

drawCirculo(50, 'Red')
forward(100)
drawCirculo(30, 'White')
left(120)
forward(220)
drawCirculo(70, 'Green')

hideturtle()
done()
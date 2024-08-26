from turtle import *
    
def drawSquare():
    pendown()
    begin_fill()
    
    for side in range(4):
        forward(100)
        left(90)
        
    end_fill()
    penup()

color("WhiteSmoke")
bgcolor("MidnightBlue")

drawSquare()
forward(110)
drawSquare()

hideturtle()
done()
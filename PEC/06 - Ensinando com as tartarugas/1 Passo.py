from turtle import *

def drarStar():
    pendown()
    begin_fill()

    for side in range(5):
        left(144)
        forward(50)
        
    end_fill()
    penup()

color("WhiteSmoke")
bgcolor("MidnightBlue")

drarStar()
forward(100)
drarStar()
left(120)
forward(150)
drarStar()

hideturtle()
done()
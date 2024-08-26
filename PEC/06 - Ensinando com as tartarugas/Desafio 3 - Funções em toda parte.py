from turtle import *
from random import *

def moveToRandomLocation():
    penup()
    setpos(randint(-400, 400),randint(-400, 400))
    pendown()

def drawCirculo(radius, starColour):
    pendown()
    begin_fill()
    
    color(starColour)
    circle(radius)
    
    end_fill()
    penup()

def drawGalaxy(numberOfStars):
    starColours = ['#058396', '#0275A6', '#827E01']
    moveToRandomLocation()
    
    for star in range(numberOfStars):
        penup()
        left(randint(-180, 180))
        forward(randint(5,20))
        
        drawCirculo(2, choice(starColours))
        
def drawConstellation(numberOfStars):
    moveToRandomLocation()
    
    for star in range(numberOfStars - 1):
        drawCirculo(randint(7,15), 'White')
        pendown()
        left(randint(-90, 90))
        forward(randint(30, 70))
        drawCirculo(randint(7, 15), 'White')
        
speed(11)
        
bgcolor("MidnightBlue")

for star in range(30):
    moveToRandomLocation()
    drawCirculo(randint(5,25), 'White')
    
for galaxy in range(3):
    drawGalaxy(40)
    
for constellation in range(2):
    drawConstellation(randint(4,7))

hideturtle()
done()
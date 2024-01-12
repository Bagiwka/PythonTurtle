from turtle import *
from math import sqrt

farben = ['red','green','blue']
winkel = ['40','-80','40']
aeste = ['30','-60']
laengen = [[200,150],[150,150*3/4]]

def Move(len, win):
    right(win)
    forward(len)

def NikoHaus(b,x,y):
    penup()
    goto(x,y)
    pendown()
    m=sqrt(b*b+b*b)
    Move(m/2,45)
    Move(b,-135)
    Move(m,-135)
    Move(b,135)
    Move(b,90)
    Move(m/2,-135)
    Move(m/2,-90)
    Move(m,-90)
    Move(b,135)

def LineWithoutMoving(len, farbe):
        color(farbe)
        forward(len)
        backward(len)

def run():

    speed(0)
    setheading(90)
    farbe=0
    win=0
    length=0
    aesteZ=0
    zaehler=0

    for triple in range(0,5):
        length=0
        for faecher in range(0,3):
            for ast in range(0,3):
                LineWithoutMoving(laengen[length][zaehler],farben[farbe])
                left(int(winkel[win])) 
                win+=1
                if win>=3:
                    win=0
                if zaehler == 0:
                    zaehler = 1
            zaehler=0
            length=1
            farbe+=1
            if farbe>=3:
                farbe=0
            left(int(aeste[aesteZ]))
            aesteZ+=1
            if aesteZ >= 2:
                aesteZ=0
        right(90)


    color('black')

    left(65)

    b = input('Geben sie die Breite ein: ')
    while not b.isnumeric():
        b = input('Breite muss eine ganze Zahl sein.\nGeben sie die Breite ein: ')
    x = input('Geben sie die x-koordinate ein: ')
    while not x.isnumeric():
        x = input('x muss eine ganze Zahl sein.\nGeben sie die x-Koordinate ein: ')
    y = input('Geben sie die y-Koordinate ein: ')
    while not y.isnumeric():
        y = input('y muss eine ganze Zahl sein.\nGeben sie die y-Koordinate ein: ')


    setheading(0)
    NikoHaus(int(b),int(x),int(y))

run()
reseter=True
while reseter:
    if input("Nochmal? ") == 'Ja':
        reset()
        run()
    else:
        reseter=False
#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor,GyroSensor,ColorSensor
from pybricks.parameters import Port, Color, SoundFile, Stop
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math


xAxis = Motor(Port.A)
yAxis = Motor(Port.B)
Pen = Motor(Port.C)
color = ColorSensor(Port.S4)

penUp = True
lengthOfPage = 10
widthOfPage = 5
xMotorRatio = 70/720 #change later
yMotorRatio = 80/720 #change later

currentx = 0
currenty = lengthOfPage

def MillimetersToDegreesX(mm):
    return mm*720/70

def MillimetersToDegreesY(mm):
    return mm*720/80

def MoveMotor(degrees, speed, name, wait):
    #move medium motor
    name.run_angle(speed, degrees, Stop.BRAKE, wait)

def penup():
    global penUp
    if penUp == False:
        MoveMotor(450, 300, Pen, True)
        penUp = True
    else:
        pass

def pendown():
    global penUp
    if penUp == True:
        MoveMotor(450, -300, Pen, True)
        penUp = False
    else:
        pass

def goto(x, y):
    global currentx
    global currenty

    xdistance =  (x - currentx)
    ydistance =  (y - currenty)
    xradius = MillimetersToDegreesX(xdistance)
    yradius = MillimetersToDegreesY(ydistance)

    if ydistance == 0:
        time = abs(xradius / 100) * 1000
        xAxis.run_time(- math.copysign(100, ydistance), time, Stop.BRAKE, False)
    else:
        speedRatio = abs((x-currentx)/(y-currenty))
        time = abs(yradius / 100) * 1000
        xAxis.run_time(speedRatio * math.copysign(100, xdistance), time, Stop.BRAKE, False)
        yAxis.run_time(- math.copysign(100, ydistance), time, Stop.BRAKE, False)

    wait(time + 1000)
    yAxis.stop(Stop.BRAKE)
    xAxis.stop(Stop.BRAKE)

    currentx = x
    currenty = y

def feedPaper():
    penup()
    yAxis.run(-100)
    c = color.reflection()

    while c < 5:
        c = color.reflection()
        print(c)
    yAxis.stop(Stop.BRAKE)

    MoveMotor(1000, 200, xAxis, True)
    currentx = 0
    currenty = 0


penUp = True
penup()



def drawbox():
    #Horizontal lines
    penup()
    goto(0, 30)
    pendown()
    goto(0, 160)

    penup()
    goto(-30, 0)
    pendown()
    goto(-30, 160)

    penup()
    goto(-60, 0)
    pendown()
    goto(-60, 160)

    penup()
    goto(-90, 30)
    pendown()
    goto(-90, 160)

    #Vertical lines

    penup()
    goto(0, 30)
    pendown()
    goto(-90, 30)

    penup()
    goto(0, 80)
    pendown()
    goto(-90, 80)

    penup()
    goto(0, 110)
    pendown()
    goto(-90, 110)

    penup()
    goto(0, 160)
    pendown()
    goto(-90, 160)

    #penup()
    #goto(0, 160)
    #pendown()
    #goto(-90, 160)





    #tab
    penup()
    goto(-60, 0)
    pendown()
    goto(-30, 0)

feedPaper()
drawbox()

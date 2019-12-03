#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align, Stop)
from botbuilder import robot

def Swing():
    robot.GoTowards(17, 0, 200)
    robot.FollowLine(21, 200)
    robot.GoTowards(8 ,0 ,200)
    robot.FollowLine(17, 200)
    robot.RealStop()
    #Start Elevator mission

    robot.TurnTo(45, 300)
    #push the thing
    robot.GoTowards(1, 45, 100)
    robot.GoBackTowards(3, 45, 100)
    robot.TurnTo(25, 300)
    robot.GoBackTowards(19, 25, 200)
    robot.RealStop()
    robot.TurnTo(-20, 300)
    robot.GoTowards(12,-25,200)
    robot.GoBack(6.5,50)
    #It's time to go back
    robot.GoBackTowards(17, -45, 300)
    robot.TurnTo(0, 300)
    robot.GoBackTowards(52, 0, 300)
    robot.RealStop()

def Elevator():
    #This program is not being used

    #Follow line
    robot.FollowLine(24,150)
    robot.GoTowards(5,0,150)
    #Turn to bridge
    robot.TurnTo(-110,150)
    robot.GoTowards(9,-110,150)
    #Go to the elevator
    robot.TurnTo(-20, 150)
    #Go forward and back
    robot.GoTowards(7,-20,75)
    robot.GoBack(6.5,50)
    robot.GoBack(20, 500)

def ColorMatch():
    robot.GoTowards(16.5, 0, 200)
    robot.FollowLine(8.5, 200)
    robot.RealStop()
    robot.TankTurnTo(-28, 100)
    robot.GoTowards(2.5, -28, 100)
    robot.GoBackTowards(2.5, -28, 100)
    robot.RealStop()
    robot.TankTurnTo(0,100)
    robot.FollowLine(12, 200)
    robot.GoTowards(9, 0, 200)
    robot.RealStop()
    robot.TurnTo(-90, 300)
    robot.GoTowards(9.5, -90, 150)
    robot.GoBackTowards(12, -90, 100)
    robot.RealStop()
    #GOBACKTIME
    robot.TankTurnTo(-180, 200)
    robot.GoTowards(62, -180, 300)

def Blocks():
    robot.gyro.reset_angle(-90)
    robot.GoTowards(19.5, -90, 150)
    robot.GoBackTowards(18, -90, 300)
    robot.RealStop()
    robot.TurnTo(0, 300)
    robot.GoBackTowards(17, 0, 300)
    robot.RealStop()
    robot.TurnTo(-90, 300)
    robot.RealStop()



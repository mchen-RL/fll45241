#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align, Stop)
from botbuilder import robot

def Swing():
    robot.GoTowards(5, 0, 100)
    robot.GoTowards(12, 0, 200)
    robot.FollowLine(21, 200)
    robot.GoTowards(8 ,0 ,200)
    robot.FollowLine(17, 200)
    robot.RealStop()

    #Innovative Architecture
    robot.TurnTo(50, 300)
    robot.GoTowards(2, 50, 100)
    robot.GoBackTowards(4, 50, 100)
    robot.TurnTo(25, 200)
    robot.RealStop()

    #Safety Factor
    robot.GoBackTowards(15, 25, 200)
    robot.TurnTo(-2, 200)
    robot.GoTowards(15, -2, 200)
    robot.GoBackTowards(12, 0, 200)
    robot.RealStop()

    #Elevator
    robot.TankTurnTo(-45, 300)
    robot.GoTowards(2.5, -90, 150)
    robot.TurnTo(-25, 300)
    robot.GoTowards(10, -25, 200)
    robot.GoBackTowards(6, -25, 50)

    #It's time to go back
    robot.GoBackTowards(18, -45, 300)
    robot.TurnTo(0, 300)
    robot.GoBackTowards(55, 0, 300)
    robot.RealStop()

def Elevator():
    #This program is not being used
    robot.GoStraight(5, 100)
    robot.GoBack(5, 100)

def ColorMatch():
    robot.GoTowards(5, 0, 100)
    robot.GoTowards(12, 0, 200)
    robot.FollowLine(8, 200)
    robot.RealStop()
    robot.TankTurnTo(-28, 100)
    robot.GoTowards(2.5, -28, 100)
    robot.GoBackTowards(2.5, -28, 100)
    robot.RealStop()
    robot.TankTurnTo(0, 100)
    robot.FollowLine(12, 200)
    robot.GoTowards(9, 0, 200)
    robot.RealStop()
    robot.TurnTo(-90, 300)
    robot.GoTowards(9.5, -90, 150)
    robot.GoBackTowards(6, -90, 100)
    robot.TurnTo(-60,300)
    robot.MoveMotor(-150, 400, False)
    robot.GoBackTowards(3, -150, 150)
    robot.TurnTo(-115, 250)
    robot.GoTowards(30, -115, 200)
    robot.RealStop()

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



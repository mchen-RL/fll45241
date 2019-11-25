#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align, Stop)
from botbuilder import robot

def Swing():
    robot.GoStraight(14, 150)
    robot.FollowLine(21, 150)
    robot.GoTowards(8 ,0 ,150)
    robot.FollowLine(17, 150)
    robot.RealStop()

    #Start Elevator mission
    robot.TurnTo(35, 150)
    #push the thing
    robot.GoTowards(1, 60, 100)
    robot.GoBack(1, 100)
    robot.TurnTo(25, 100)
    robot.GoBackTowards(25, 25, 150)
    robot.RealStop()
    robot.TurnTo(-20, 150)
    robot.GoTowards(7.5,-25,75)
    robot.GoBack(6.5,50)
    robot.GoBack(45, 450)
    robot.TankTurnTo(0, 150)
    robot.GoBack(10, 100)
    robot.RealStop()
    robot.TankTurnTo(-90, 100)





def Elevator():
    #This program is not being used people, don't use it. It's already being combined with the swing.
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
    robot.GoTowards(14, 0, 150)
    robot.FollowLine(7, 150)
    robot.RealStop()
    robot.TankTurnTo(-20, 100)
    robot.GoTowards(2, -20, 100)
    robot.GoBackTowards(2.5, -20, 100)
    robot.RealStop()
    robot.TankTurnTo(0,100)
    robot.FollowLine(12,150)
    robot.GoTowards(10, 0, 150)
    robot.RealStop()
    robot.TurnTo(-90, 100)
    robot.GoTowards(10, -90, 100)
    robot.GoBack(10, 100)
    robot.RealStop()

def Blocks():
    robot.GoStraight(18.5, 100)
    robot.GoBack(17,200)
    robot.RealStop()
    robot.TurnRight(90, 200)
    robot.GoBack(15, 200)
    robot.RealStop()
    robot.TankTurnLeft(100, 200)
    robot.RealStop()



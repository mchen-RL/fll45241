#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot

def Swing():
    robot.GoStraight(14, 150)
    robot.Debug(1)
    robot.FollowLine(21, 150)
    robot.Debug(2)
    robot.GoStraight(5,150)
    robot.Debug(3)
    robot.TurnTo(-50, 150)
    robot.Debug(4)
    robot.GoTowards(10, -50, 150)
    robot.Debug(5)
    robot.TurnTo(55, 150)
    robot.Debug(6)
    robot.GoTowards(10, 55, 150)
    robot.Debug(7)
    robot.TurnTo(0, 150)
    robot.Debug(8)
    robot.GoTowards(5, 0, 150)
    robot.Debug(9)
    robot.GoBack(50,450)

def SwingElevator():

    #Elevator
    robot.FollowLine(24,150)
    robot.GoTowards(5,0,150)
    robot.TurnTo(-110,150)
    robot.GoTowards(9,-110,150)
    robot.TurnTo(-20, 150)
    robot.GoTowards(4.5,-20,75)
    robot.GoBack(4.5, 75)

    #Swing
    robot.TurnTo(55, 150)
    robot.GoTowards(10, 55, 150)
    robot.TurnTo(0, 150)
    robot.GoTowards(5, 0, 150)
    robot.GoBack(50,450)



def Elevator():
    #Follow line
    robot.TurnTo(0,150)
    robot.FollowLine(24,150)
    robot.GoTowards(5,0,150)
    #Turn to bridge
    robot.TurnTo(-110,150)
    robot.GoTowards(9,-110,150)
    #Go to the elevator
    robot.TurnTo(-20, 150)
    #Go forward and back
    robot.GoTowards(7,-20,75)
    robot.GoBack(7,75)
    robot.GoBack(40, 500)

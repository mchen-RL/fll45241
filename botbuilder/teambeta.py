#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot

def M07Swing():
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


def Elevator():
    robot.TurnTo(0,150)   
    robot.FollowLine(29,150) 
    robot.TurnTo(-110,150)
    robot.GoTowards(10,-110,150)
    robot.TurnTo(-20, 150)
    robot.GoTowards(4.5,-20,75)
    robot.GoBack(12, 75)

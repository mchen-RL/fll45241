#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot

def M07Swing():
    robot.GoStraight(12, 150)
    robot.FollowLine(24, 150)
    robot.TurnLeft(40, 150)
    robot.GoStraight(10, 150)
    robot.TurnRight(70, 150)
    robot.GoStraight(8, 150)
    robot.TurnLeft(35, 150)
    robot.GoStraight(7, 150)
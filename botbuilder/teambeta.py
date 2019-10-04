#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot

def M07Swing():
    robot.GoStraight(14, 150)
    robot.FollowLine(21, 150)
    robot.GoStraight(5,150)
    robot.TurnTo(-50, 150)
    robot.GoStraight(10, 150)
    robot.TurnTo(45, 150)
    robot.GoStraight(11, 150)
    robot.TurnTo(0, 150)
    robot.GoStraight(5, 150)
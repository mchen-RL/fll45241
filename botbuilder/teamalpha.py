#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot
# Rowan is a bot
def Crane():
   robot.GoStraight(25,150)
   robot.GoBack(12,150)
   robot.TurnRight(90,150)
   robot.GoStraight(2,150)
   robot.TurnLeft(87,150)
   robot.GoStraight(6,100)
   robot.GoBack(0.5,50)

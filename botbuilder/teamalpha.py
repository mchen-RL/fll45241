#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot

def Crane():
   robot.GoStraight(25,150)
   robot.GoBack(12,150)
   robot.TurnRight(90,150)
   robot.GoStraight(3,150)
   robot.TurnLeft(45,150)
   robot.GoStraight(9,100)

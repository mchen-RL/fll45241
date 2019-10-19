#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot
# Rowan is a bot0
def Crane():
   robot.gyro.reset_angle(-90)
   robot.GoTowards(25,-90,150)
   robot.GoBack(12,150)
   robot.TurnTo(0,150)
   robot.GoTowards(3,0,150)
   robot.TurnTo(-90,150)
   robot.GoTowards(3,-90,150)
   robot.GoTowards(3,-90,50)
   robot.GoBack(0.5,50)
   robot.MoveMotor(150,80)

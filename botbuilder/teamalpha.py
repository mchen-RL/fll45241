#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot

def Crane():
   robot.gyro.reset_angle(-90)
   robot.GoTowards(26.5,-90,200)
   robot.GoTowards(2.7,-90,50)
   robot.GoBackTowards(12,-90,200)
   robot.RealStop()
   #Go to the next lever
   robot.TurnTo(0,300)
   robot.GoTowards(4,0,200)
   robot.RealStop()
   robot.TurnTo(-90,300)
   robot.GoTowards(3,-90,150)
   robot.GoTowards(2,-90,28)
   robot.GoBack(0.5,50)
   robot.RealStop()
   wait(500)
   #Do multiple lifts for different enviroments
   robot.MoveMotor(110, 400, True)
   robot.MoveMotor(125, 400, True)
   robot.MoveMotor(140, 400, True)
   robot.MoveMotor(150, 400, False)
   wait(500)
   robot.MoveMotor(-150, 400, False)

   #It's time to go back!
   robot.GoBackTowards(10, -90, 300)
   robot.GoBackTowards(40, 0, 300)
   robot.RealStop()

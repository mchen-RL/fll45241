#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align, Stop)
from botbuilder import robot

def Swing():
    robot.GoTowards(5, 0, 100)
    robot.GoTowards(12, 0, 250)
    robot.FollowLine(21, 250)
    robot.GoTowards(8 ,0 ,250)
    robot.FollowLine(17, 250)
    robot.RealStop()

    #Innovative Architecture
    robot.TurnTo(50, 300)
    robot.GoTowards(2, 50, 100)
    robot.GoBackTowards(4, 50, 100)
    robot.TurnTo(25, 200)
    robot.RealStop()

    #Safety Factor
    robot.GoBackTowards(16, 25, 250)
    robot.TurnTo(0, 250)
    robot.GoTowards(18, 0, 250)
    robot.GoBackTowards(12, 0, 250)
    robot.RealStop()

    #Elevator
    robot.TankTurnTo(-45, 300)
    robot.GoTowards(1.5, -45, 150)
    robot.TurnTo(-25, 300)
    robot.GoTowards(12, -25, 250)
    robot.GoBackTowards(6, -25, 50)

    #It's time to go back
    robot.GoBackTowards(5, -25, 300)
    robot.GoBackTowards(65, 0, 300)
    robot.RealStop()

def ColorMatch(add):
    # go to the red circle
    robot.GoTowards(5, 0, 100)
    robot.GoTowards(12, 0, 250)
    robot.FollowLine(8, 250)
    robot.RealStop()
    robot.TankTurnTo(-28, 100)
    robot.GoTowards(2.7, -28, 100)
    robot.GoBackTowards(2.5, -28, 100)
    robot.RealStop()
    # go to the tan circle
    robot.TankTurnTo(0, 100)
    robot.FollowLine(12, 250)
    robot.GoTowards(9, 0, 250)
    robot.RealStop()
    robot.TurnTo(-90, 300)
    robot.GoTowards(9.5, -90, 150)
    robot.GoBackTowards(6, -90, 100)
    # drop the attachment
    robot.TurnTo(-60,300)
    robot.MoveMotor(-150, 400, False)
    robot.GoBackTowards(5.5, -60, 200)
    # go ramp
    robot.TurnTo(-120, 250)
    if add:
        robot.GoTowards(35, -120, 200)
    else:
        robot.GoTowards(25, -120, 200)
    robot.RealStop()

def Blocks():
    robot.gyro.reset_angle(-90)
    robot.GoTowards(20, -90, 250)
    robot.GoBackTowards(7, -90, 300)
    robot.RealStop()
    robot.GoBackTowards(22, 0, 250)
    robot.RealStop()
    robot.TurnTo(-90,300)
    robot.RealStop()



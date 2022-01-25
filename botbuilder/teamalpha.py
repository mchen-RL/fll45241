#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot


def Testie():
    robot.GoTowards(40, 0, 200)
    robot.TurnTo(90, 200)
    robot.GoTowards(3, 90, 200)
    robot.TurnTo(180, 200)
    robot.TurnTo(0, 200)
    robot.GoBackTowards(40, 0, 200)

def Bridge():
   robot.GoStraignt(7, 200)
   robot.FollowLine(50, 200)
   #robot.GoStraight(18.5, 200)
   #robot.TurnRight(85, 75)
   #robot.GoStraight(45, 200)
   robot.GoBack(60, 200) 

def UnusedCapacity():
   robot.GoStraight(21, 200)
   robot.TankTurnRight(90, 100)
   robot.GoBack(15,200)

def Helicopter():
   robot.GoStraight(7,200)
   robot.TankTurnRight(20,100)
   robot.FollowLine(65,100) 
   robot.TankTurnRight(180,100)
   robot.GoBack(5,100)

def PlatooningTrucks():
   robot.GoStraight(14, 200)
   robot.TankTurnRight(90, 150)
   robot.GoTowards(20, 90, 100)
   robot.GoBack(45, 200)


def Plane():
   robot.GoTowards(24.8,0,200)
   robot.TankTurnTo(-45,150)
   robot.GoTowards(2.5,-45,200)
   robot.MoveMotor(360, -200, False)
   robot.MoveMotor(360, 200, False)

def test():
   robot.MoveMotor(160, -200, False)
   robot.wait(2000) 
   robot.MoveMotor(160, 200, False)

def Run2():

   #Helicopter, Train Tracks, Bridge,  Blue block
   robot.gyro.reset_angle(0)

   #Bridge
   robot.GoStraight(7,200)
   robot.TankTurnRight(20,120)
   robot.FollowLine(21, 120) 
   robot.GoTowards(20, 90, 200)

   #Crane
   robot.TankTurnTo(180,120)
   robot.GoBackTowards(5, 180, 200)
   robot.TankTurnTo(270, 120)
   robot.GoBackTowards(8, 270, 200)
   robot.GoBackTowards(8, 290, 80)

   #Helicopter
   robot.TankTurnTo(235, 100)
   robot.GoBackTowards(11, 250, 200)
   
   #Blue block
   robot.GoTowards(7, 210, 200)
   robot.TankTurnTo(360, 200, False)
   robot.GoBackTowards(2, 360, 120)
   robot.MoveMotor(140, -120, False)
   robot.MoveMotor(140, 200, False)


def Run1():
   #Box Delivery, Sorting Center, Innovation Model

   #Box Delivery
   robot.gyro.reset_angle(-90)
   robot.GoBackTowards(37, -90, 200)
   robot.TankTurnTo(-60, 120)
   robot.GoBackTowards(11, -60, 150)                       
   robot.GoBackTowards(4, -90, 100)
   robot.GoTowards(2, -90, 100)

   #Innovation Model 
   robot.GoTowards(12, -50, 150)
   robot.GoBackTowards(15, -120, 150)
   robot.MoveMotor(90, 200, False)

   #Sorting Center
   robot.GoBackTowards(5.5, -120, 150)
   robot.TankTurnTo(-180, 120)
   robot.GoBackTowards(5, -180, 150)
   robot.MoveMotor(130, 200, False)
   robot.MoveMotorTime(200, 100)
   robot.GoTowards(12, -180, 100)
   robot.GoBackTowards(1, -180, 150)
   #robot.MoveMotor(-200, 250, False)
   robot.MoveMotorTime(1000, -300)
   robot.TankTurnTo(-180, 100)
   robot.GoBackTowards(7, -180, 200)

   #go home
   robot.TankTurnTo(-90, 150)
   robot.GoTowards(39, -90, 250)
   robot.TankTurnTo(-135, 100)
   robot.GoTowards(14, -135, 250)
   robot.TankTurnTo(-60, 100)
   robot.GoTowards(27, -60, 250)
   robot.GoTowards(3, 0, 100)
   
#   ____     ____ 
#  (>^<^)> <(^>^<) - Hugs from chicken
  
def Run3():
   robot.GoTowards(14, 0, 200)
   robot.FollowLine(15, 120)
   robot.GoTowards(6, 45, 200)
   robot.GoBackTowards(8.5, 45, 150)
   robot.MoveMotorTime(800, 300)
   wait(1000)
   robot.GoBackTowards(4, 45, 120)
   robot.MoveMotorTime(500, -300)
   robot.TurnTo(0, 200, False)
   robot.GoBackTowards(22, 0, 300)

def Run4():
   robot.gyro.reset_angle(0)

   #Truck
   robot.GoTowards(12.5, 0, 200)
   robot.TurnTo(92, 200, False)
   robot.GoTowards(10, 90, 200) 
   robot.GoTowards(4.5, 90, 100)
   robot.GoBackTowards(8.5, 90, 200)

   robot.TankTurnTo(75, 200, False)
   robot.FollowLine(24, 150)
   robot.TankTurnTo(0, 120)
   robot.GoTowards(15, 0, 200)

   robot.TankTurnTo(-90, 200)
   robot.GoTowards(4, -90, 200) 
   robot.GoTowards(4, -90, 30) 
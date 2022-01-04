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
   robot.GoStraight(7,180)
   robot.TankTurnRight(20,120)
   robot.FollowLine(41,120) 

   #Crane
   robot.TankTurnTo(180,120)
   robot.GoBackTowards(5.5, 180, 120)
   robot.TankTurnTo(270, 120)
   robot.GoBackTowards(8, 270, 200)
   robot.GoBackTowards(10, 290, 80)

   #Helicopter
   robot.TankTurnTo(240, 100)
   robot.GoBackTowards(11, 240, 120)
   
   #Blue block
   robot.wait(2000)
   robot.GoTowards(8, 210, 120)
   robot.TankTurnTo(360, 150)
   robot.GoBackTowards(3, 360, 120)
   robot.MoveMotor(140, -150, False)
   robot.MoveMotor(140, 200, False)
   robot.wait(2000)

   #Go back
   robot.TankTurnTo(270, 150)
   robot.GoTowards(37, 270, 200)
   robot.TankTurnTo(225, 150)
   robot.GoTowards(36, 225, 200)

   #Train Tracks
   
   # robot.TankTurnTo(180, 100)
   # robot.GoTowards(17, 180, 200)
   # robot.TankTurnTo(90, 100)
   # robot.GoStraight(1, 100)
   # robot.MoveMotor(270, -200, False) 
   # robot.GoBackTowards(10,-90, 200)
   # robot.MoveMotor(270, 200, False)   

   # #Go Back
   # robot.TankTurnTo(-135, 100)
   # robot.GoTowards(4, -135, 200)
   # robot.GoTowards(60,-90, 200)

def Run1():
   #Box Delivery, Sorting Center, Innovation Model

   #Box Delivery
   robot.gyro.reset_angle(-90)
   robot.GoBackTowards(2, -90, 100)
   robot.GoBackTowards(35, -90, 200)
   robot.TankTurnTo(-60, 120)
   robot.GoBackTowards(13.5, -60, 150)
   robot.TankTurnTo(-85, 100)                          
   robot.GoBackTowards(1.5, -85, 100)
   robot.GoTowards(1.5, -85, 100)

   #Innovation Model 
   robot.TankTurnTo(-50, 100)
   robot.GoTowards(11, -50, 150)
   robot.GoBackTowards(15, -120, 100)
   robot.MoveMotor(80, 200, False)

   #Sorting Center
   robot.GoBackTowards(3, -120, 150)
   robot.TankTurnTo(-180, 100)
   robot.GoBackTowards(5, -180, 150)
   robot.MoveMotor(145, 200, False)
   robot.GoTowards(12, -180, 150)
   robot.GoBackTowards(1, -180, 150)
   robot.MoveMotor(-165, 200, False)
   robot.GoBackTowards(9, -180, 150)

   #go home
   robot.TankTurnTo(-90, 100)
   robot.GoTowards(37, -90, 150)
   robot.TankTurnTo(-135, 100)
   robot.GoTowards(4, -135, 150)
   robot.TankTurnTo(-90, 100)
   robot.GoTowards(5, -90, 200)
   robot.GoTowards(10, -90, 200)
   robot.TankTurnTo(-60, 100)
   robot.GoTowards(15, -60, 200)
   robot.TankTurnTo(0, 100)
   
#   ____     ____ 
#  (>^<^)> <(^>^<) - Hugs from chicken
   
# def SortingCenter():
#    robot.GoTowards(8, 0, 120)
#    robot.TankTurnTo(90, 120)
#    robot.GoTowards(45, 90, 120)
#    robot.TankTurnTo(0, 120)
#    robot.GoTowards(14, 0 , 120)
#    robot.TankTurnTo(90, 120)
#    robot.GoTowards(12 ,90, 120)
#    robot.TankTurnTo(180, 120)
#    robot.MoveMotor(250, 200, False)
#    robot.GoTowards(25, 180, 120)
#    robot.GoBack(0.7, 120)
#    robot.MoveMotor(270, -200, False)
#    robot.GoBack(5, 80)
#    robot.TankTurnTo(270, 150)
#    robot.GoTowards(36, 270, 120)
#    robot.TankTurnTo(225, 150)
#    robot.GoStraight(5, 150)
#    robot.TankTurnTo(270, 150)
#    robot.GoTowards(40, 270, 300)

def Switch():
   robot.GoStraight(14,120)
   robot.FollowLine(23,120)
   robot.TurnTo(80,100)
   robot.GoStraight(1,120)
   robot.MoveMotor(-180, 100, False)
   robot.GoBack(3,120)

   
def Run3():
   robot.GoTowards(14, 0, 120)
   robot.FollowLine(15, 120)
   robot.GoStraight(6, 120)
   robot.GoBack(9, 170)
   robot.MoveMotor(120, 100, False)
   wait(3000)
   robot.GoBack(4, 170)
   robot.MoveMotor(-120, 100, False)
   wait(3000)
   robot.GoBack(4, 170)


def Run4():
   robot.gyro.reset_angle(0)

   #Truck
   robot.GoStraight(12.2,180)
   robot.TurnTo(93,180)
   robot.GoTowards(15, 90, 120) 
   robot.GoBackTowards(9, 90, 100)
   robot.TankTurnTo(70,120)
   robot.FollowLine(24,120)
   robot.TankTurnTo(0,120)
   robot.GoTowards(14,0,120)

   robot.TankTurnTo(-90,120)
   robot.GoTowards(6, -90, 120) 
   robot.GoTowards(4, -90, 70) 
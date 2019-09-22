#!/usr/bin/env pybricks-micropython

# import more Classes for us to use
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor,GyroSensor,ColorSensor
from pybricks.parameters import (Port, SoundFile)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math

# "=" is called assignments. It creates "variables"
# You can think of variables as boxes with a name on it, you can put values in it
# and later get them out to use.
# - create a variable (box) called "left", and put a Motor on Port B in it.
# - create another variable called "right", and put a Motor on Port C in it.
# - create a 3rd variable called "robot", and tell it which motors drive the wheels 
#   and how big the robot is.
left = Motor(Port.B)
right = Motor(Port.C)
wheel_diameter=56
robot = DriveBase(left, right, wheel_diameter, 114)
color1 = ColorSensor(Port.S1)
color2 = ColorSensor(Port.S2)
gyro = GyroSensor(Port.S3)

# pi * diameter(radius * 2)
def InchToDegrees(inch):
    mm = inch * 25.4
    rotation =  math.pi * wheel_diameter
    degrees = (mm/rotation) * 360
    return degrees

def GoStraight(inch, speed):
    robot.drive(speed, 0)
    degrees = InchtoDegrees(inch)
    robot.reset_angle(0)
    while(right.angle() < degree):
        pass
    robot.stop(Stop.BRAKE)

def FollowLine(inch, speed):
    def GoStraight(inch, speed):
    robot.drive(speed, 0)
    degrees = InchtoDegrees(inch)
    robot.reset_angle(0)
    while(right.angle() < degree):
        ColorReflect = colorf1.reflection()
        error = ColorReflect - 40
        robot.drive(speed,error)
    robot.stop(Stop.BRAKE)


def TurnLeft(degrees, speed):
    CurrentDegrees = gyro.degree()
    left.stop(Stop.BRAKE)
    right.run(speed)
    stopDegree = CurrentDegrees - degree
    while (gyro.degree() > stopDegree):
        pass
    robot.stop(Stop.BRAKE)

def TurnRight(degrees, speed):
    CurrentDegrees = gyro.degree()
    right.stop(Stop.BRAKE)
    left.run(speed)
    stopDegree = CurrentDegrees + degree
    while (gyro.degree() < stopDegree):
        pass
    robot.stop(Stop.BRAKE)


    
    
#!/usr/bin/env pybricks-micropython

# import more Classes for us to use
import math
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.parameters import (Port, Stop, SoundFile)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# "=" is called assignments. It creates "variables"
# You can think of variables as boxes with a name on it, you can put values in it
# and later get them out to use.
# - create a variable (box) called "left", and put a Motor on Port B in it.
# - create another variable called "right", and put a Motor on Port C in it.
# - create a 3rd variable called "driver", and tell it which motors drive the wheels 
#   and how big the robot is.
left = Motor(Port.B)
right = Motor(Port.C)
gyro = GyroSensor(Port.S4)
color1 = ColorSensor(Port.S1)
color2 = ColorSensor(Port.S2)
diameter = 56
driver = DriveBase(left, right, diameter, 114)

# you can create your own function with "def" 
# this is the way to teach the robot new tricks
# - this function makes the robot go straight forward until the wheels turn a number of rotations
def drive_straight(rotations, power = 200):
    # let's use left motor the tell us how many rotations we have done
    # to do this, first we need to set its degree memory to zero
    left.reset_angle(0)
    # start moving straight forward
    driver.drive(power, 0)
    # keep checking until we turned enough
    # one rotation is 360 degrees so we multiple by 360
    # "while" creates a loop that repeats until the check fails
    while left.angle() < 360 * rotations:
        # we don't really have anything to do when waiting so just "pass"
        pass
    # we are done with rotations, stop the robot
    driver.stop(Stop.BRAKE)

# drive straight in inches
def drive_inch(inches, power = 200):
    # calc degrees from distance
    circumference = diameter * math.pi
    rotation = inches * 25.4 / circumference
    drive_straight(rotation, power)

def follow_line(inches):
    circumference = diameter * math.pi
    rotations = inches * 25.4 / circumference
    # let's use left motor the tell us how many rotations we have done
    # to do this, first we need to set its degree memory to zero
    left.reset_angle(0)
    # start moving straight forward
    driver.drive(200, 0)
    # keep checking until we turned enough
    # one rotation is 360 degrees so we multiple by 360
    # "while" creates a loop that repeats until the check fails
    while left.angle() < 360 * rotations:
        correct = (color2.reflection() - 40) * 0.5
        driver.drive(200, correct)
    # we are done with rotations, stop the robot
    driver.stop(Stop.BRAKE)

def drive_to(degree, inches):
    circumference = diameter * math.pi
    rotations = inches * 25.4 / circumference
    # let's use left motor the tell us how many rotations we have done
    # to do this, first we need to set its degree memory to zero
    left.reset_angle(0)
    # start moving straight forward
    driver.drive(200, 0)
    # keep checking until we turned enough
    # one rotation is 360 degrees so we multiple by 360
    # "while" creates a loop that repeats until the check fails
    while left.angle() < 360 * rotations:
        err = (degree - gyro.degree()) * 0.5
        driver.drive(200, - err)
    # we are done with rotations, stop the robot
    driver.stop(Stop.BRAKE)

# def another function that make the robot turn 90 degrees right
# the best way to do this is to use the Gyro sensor to tell us how much 
# the robot has turned
def turn_right(degrees, power = 200):
    adjustment = 8
    # in order to turn right, we stop the right motor and drive the left one
    right.stop()
    left.run(power)
    # we want to keep turning until the gyro gets an angle that's larger than 90
    start = gyro.angle()
    while(gyro.angle() < degrees + start - adjustment):
        pass
    # turn off motors
    driver.stop(Stop.BRAKE)

# def another function that make the robot turn 90 degrees right
# the best way to do this is to use the Gyro sensor to tell us how much 
# the robot has turned
def turn_left(degrees, power = 200):
    adjustment = 8
    # in order to turn right, we stop the right motor and drive the left one
    left.stop()
    right.run(power)
    # we want to keep turning until the gyro gets an angle that's larger than 90
    start = gyro.angle()
    while(gyro.angle() > start - degrees + adjustment):
        pass
    # turn off motors
    driver.stop(Stop.BRAKE)

# turn to a particular degree by compass
def turn_to(degree, power = 200):
    adjustment = 8
    start = gyro.angle()
    if start < degree:
        turn_right(degree - start, power)
    else:
        turn_left(start - degree, power)



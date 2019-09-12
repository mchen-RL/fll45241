#!/usr/bin/env pybricks-micropython

# import more Classes for us to use
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import (Port, Stop, SoundFile)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# "=" is called assignments. It creates "variables"
# You can think of variables as boxes with a name on it, you can put values in it
# and later get them out to use.
# - create a variable (box) called "left", and put a Motor on Port B in it.
# - create another variable called "right", and put a Motor on Port C in it.
# - create a 3rd variable called "robot", and tell it which motors drive the wheels 
#   and how big the robot is.
left = Motor(Port.B)
right = Motor(Port.C)
gyro = GyroSensor(Port.S4)
robot = DriveBase(left, right, 56, 114)

# you can create your own function with "def" 
# this is the way to teach the robot new tricks
# - this function makes the robot go straight forward until the wheels turn a number of rotations
def drive_straight(rotations):
    # let's use left motor the tell us how many rotations we have done
    # to do this, first we need to set its degree memory to zero
    left.reset_angle(0)
    # start moving straight forward
    robot.drive(250, 0)
    # keep checking until we turned enough
    # one rotation is 360 degrees so we multiple by 360
    # "while" creates a loop that repeats until the check fails
    while left.angle() < 360 * rotations:
        # we don't really have anything to do when waiting so just "pass"
        pass
    # we are done with rotations, stop the robot
    robot.stop()

# def another function that make the robot turn 90 degrees right
# the best way to do this is to use the Gyro sensor to tell us how much 
# the robot has turned
def turn_right_90():
    # in order to turn right, we stop the right motor and drive the left one
    right.stop()
    left.run(160)
    # we want to keep turning until the gyro gets an angle that's larger than 90
    start = gyro.angle()
    while(gyro.angle() < 85 + start):
        pass
    # turn off motors
    robot.stop(Stop.BRAKE)
    wait(100)
    print(gyro.angle())

# make some noise
brick.sound.file(SoundFile.HELLO)

# drive forward 2 rotations and then make a right 90 degree turn
# then forward another 2 rotation and turn again
drive_straight(2)
turn_right_90()
drive_straight(2)
turn_right_90()
drive_straight(2)

# make some noise
brick.sound.file(SoundFile.KUNG_FU)


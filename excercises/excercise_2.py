#!/usr/bin/env pybricks-micropython

# import more Classes for us to use
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, SoundFile)
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
robot = DriveBase(left, right, 56, 114)

# make some noise
brick.sound.file(SoundFile.HELLO)

# call "drive_time" function on the robot we just created with 3 parameters
# - drive speed (how fast)
# - steering, or turning (0 means going straight)
# - for how long (2000 = 2000 miliseconds = 2 seconds)
robot.drive_time(250, 0, 2000)

# after 2 seconds make the robot stop
robot.stop()

# make some noise
brick.sound.file(SoundFile.KUNG_FU)


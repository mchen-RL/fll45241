#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from missions import robot

# drive forward 2 rotations and then make a right 90 degree turn
# then forward another 2 rotation and turn again
def Rowan():
    robot.drive_inch(12)
    robot.drive_inch(24)
    robot.turn_left(40)
    robot.drive_inch(10)
    robot.turn_right(70)
    robot.drive_inch(8)
    robot.turn_left(35)
    robot.drive_inch(7)

def coach():
    robot.drive_inch(12)
    robot.follow_line(20)
    robot.drive_inch(7)
    robot.turn_to(-40)
    robot.drive_inch(9)
    robot.turn_to(40)
    robot.drive_inch(6)
    robot.turn_to(0, 300)
    robot.drive_inch(7, 300)

def clara():
    robot.drive_inch(2.5)
    robot.turn_left(90)
    robot.drive_inch(22)

# Write your program here
w = StopWatch()
coach()
print(w.time())
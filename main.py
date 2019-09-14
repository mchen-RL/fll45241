#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from missions import robot

# drive forward 2 rotations and then make a right 90 degree turn
# then forward another 2 rotation and turn again
robot.drive_inch(2)
robot.turn_left(90)
robot.drive_inch(21)






# Write your program here
brick.sound.beep()
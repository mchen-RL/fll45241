#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from missions import robot

# drive forward 2 rotations and then make a right 90 degree turn
# then forward another 2 rotation and turn again
robot.drive_inch(12)
robot.drive_inch(22)
robot.turn_left(50)
robot.drive_inch(8)
robot.turn_right(50)
robot.drive_inch(10)
robot.turn_left(35)
robot.drive_inch(7)

# Write your program here
brick.sound.beep()

#Hello whoever got this is very lucky 
#because they got to swing!!!!!!!!!!
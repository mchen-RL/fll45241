#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
# Initialize two motors and a drive base
color = ColorSensor(Port.S2)
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 56, 114)

#line follow
def follow_line():
    left.reset_angle(0)
    while(left.angle() < 2000):
        adjust = (color.reflection() - 40) * 1.0
        robot.drive(160, adjust)
    robot.stop()

# Drive forward until an object is detected
brick.sound.file(SoundFile.HELLO)
robot.drive_time(250, 0, 2200)
follow_line()
robot.stop()
brick.sound.file(SoundFile.KUNG_FU)


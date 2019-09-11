#!/usr/bin/env pybricks-micropython

# "from...import" is Python way of bringing in someone else's program
# so that you can use it. In this case we are bringing in what LEGO provided
# for Python (called pybricks).
# for example: this line means we will bring in the ev3brick and call it "brick"
# - the programs from which you import are called "libraries"
# - the things you bring in (for example ev3brick) are called "classes"
# - you use those classes by "calling" a "function" on them (we will see examples later)
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# 
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


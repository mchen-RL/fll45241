#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot, teamalpha as alpha, teambeta as beta

missions = ["Images/Swing.png", "Images/Elevator.jpg", "Images/Crane.jpg",
            "Images/StackBlocks.jpg", "Images/ColorMatch.png","Images/Ramp.jpg"]

CurrentMission = 0
brick.display.image(missions[CurrentMission])

while True:
    # Wait until any of the buttons are pressed
    while not any(brick.buttons()):
        wait(10)

    if Button.DOWN in brick.buttons():
        print("It's time for the DOWN BUTTON")
        CurrentMission += 1
        if len(missions) == CurrentMission:
            CurrentMission = 0

    elif Button.UP in brick.buttons():
        print("It's time for the UP BUTTON")
        CurrentMission -= 1
        if -1 == CurrentMission:
            CurrentMission = len(missions) - 1

    elif Button.CENTER in brick.buttons():
        wait(100)
        robot.gyro.reset_angle(0)
        print("It's time to RUN")
        if CurrentMission == 0:
            beta.Swing()
        elif CurrentMission == 1:
            beta.Elevator()
        elif CurrentMission == 2:
            alpha.Crane()
        elif CurrentMission == 3:
            beta.Blocks()
        elif CurrentMission == 4:
            beta.ColorMatch()
        elif CurrentMission == 5:
            alpha.Ramp()

    brick.display.image(missions[CurrentMission])

    # Wait until all buttons are released
    while any(brick.buttons()):
        wait(10)

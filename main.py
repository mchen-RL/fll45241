#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot, teamalpha as alpha, teambeta as beta
missions = [
 "Images/gift.jpg", "Images/Ramp.jpg", "Images/StackBlocks.jpg", "Images/truck.jpg"]
time = StopWatch()
Start = False
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
        if Start == False:
            time.reset()
        wait(100)
        robot.gyro.reset_angle(0)
        print("It's time to RUN")
        print("Mission Started. Your time was", time.time() // 1000)

        Start = True
       if CurrentMission = 0:
           alpha.Testie()

       elif CurrentMission = 1:
            alpha.Run1()
        
       elif CurrentMission = 2:
            alpha.Run2()

        elif CurrentMission = 3:
            alpha.Run3()
        
        elif CurrentMission = 4:
            alpha.Run4()

        print(" ")
        print("Mission Accomplished! Your time was ", time.time() // 1000)
        robot.RealStop()
        robot.amotor.stop()
        CurrentMission += 1

        if len(missions) == CurrentMission:
            CurrentMission = 0

        
    brick.display.image(missions[CurrentMission])

    # Wait until all buttons are released
    while any(brick.buttons()):
        wait(10)

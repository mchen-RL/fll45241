#!/usr/bin/env pybricks-micropython

# import more Classes for us to use
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor,GyroSensor,ColorSensor
from pybricks.parameters import Port, SoundFile, Stop
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math


left = Motor(Port.B)
right = Motor(Port.C)
wheel_diameter=56
robot = DriveBase(left, right, wheel_diameter, 114)
color1 = ColorSensor(Port.S1)
color2 = ColorSensor(Port.S2)
gyro = GyroSensor(Port.S4)
time = StopWatch()
amotor = Motor(Port.A)

# pi * diameter(radius * 2)

#convert inches to degrees
def InchToDegrees(inch):
    #converts inches to millimeters
    mm = inch * 25.4
    #circumference
    rotation =  math.pi * wheel_diameter
    degrees = (mm/rotation) * 360
    return degrees

def GoStraight(inch, speed):
    degree = InchToDegrees(inch)
    #convert inches to degrees
    right.reset_angle(0)
    #reset motor rotation
    robot.drive(speed, 0)
    #go straight
    while(right.angle() < degree):
        pass
    robot.stop(Stop.BRAKE)

def FollowLine(inch, speed):
    #follows the line
    degree = InchToDegrees(inch)
    #convert inches to degrees
    right.reset_angle(0)
    #reset angle for right motor
    robot.drive(speed, 0)
    #go
    while(right.angle() < degree):
        ColorReflect = color2.reflection()
        #print(ColorReflect)
        #Color reflect = reflection from color sensor
        error = ColorReflect - 25
        #25 is in the middle of black and white, where you want to go
        #the error is how much you need to turn
        scale = speed/50
        robot.drive(speed,error * scale)
        #turning
    robot.stop(Stop.BRAKE)
    #stop



def GoTowards(inch,direction,speed):
     #uses compass to turn to degrees
    degree = InchToDegrees(inch)
    #convert inches to degrees
    right.reset_angle(0)
    #reset motor rotation
    robot.drive(speed, 0)
    #go
    while(right.angle() < degree):
        GyroCompass = gyro.angle()
        #GyroCompass = Where the robot is facing
        error = direction - GyroCompass
        #GyroCompass - direction is the error
        #the error is how much you need to turn
        robot.drive(speed,error*2)
        #turning
    robot.stop(Stop.BRAKE)
    #stop

#Makes the robot turn left
def TurnLeft(degree, speed):
    CurrentDegrees = gyro.angle()
    left.stop(Stop.BRAKE)
    right.run(speed)
    stopDegree = CurrentDegrees - degree
    while (gyro.angle() > stopDegree):
        if abs(gyro.angle() - stopDegree) < 20:
            right.run(80)
    robot.stop(Stop.BRAKE)

def TurnTo(direction,speed):
    CurrentGyro = gyro.angle()
    if CurrentGyro - direction < 0:
        TurnRight(direction - CurrentGyro, speed)
    else:
        TurnLeft(CurrentGyro - direction, speed)
    RealStop()

#Makes the robot turn right
def TurnRight(degree, speed):
    CurrentDegrees = gyro.angle()
    right.stop(Stop.BRAKE)
    left.run(speed)
    stopDegree = CurrentDegrees + degree
    while (gyro.angle() < stopDegree):
        if abs(gyro.angle() - stopDegree) < 20:
            left.run(80)

    robot.stop(Stop.BRAKE)

#it debugs when there's BIG problems
def Debug(step):
    print(step, "  gyro =", gyro.angle(),"  right rotation =", right.angle(), "left rotation =", left.angle(),"time =", time.time()//1000)

def GoBack(inch, speed):
    degree = InchToDegrees(inch)
    #convert inches to degrees
    right.reset_angle(0)
    #reset motor rotation
    robot.drive(-speed, 0)
    #go straight
    while(-right.angle() < degree):
        pass
    robot.stop(Stop.BRAKE)

def GoBackTowards(inch,direction,speed):
     #uses compass to turn to degrees
    degree = InchToDegrees(inch)
    #convert inches to degrees
    right.reset_angle(0)
    #reset motor rotation
    robot.drive(-speed, 0)
    #go
    while(-right.angle() < degree):
        GyroCompass = gyro.angle()
        #GyroCompass = Where the robot is facing
        error = direction - GyroCompass
        #GyroCompass - direction is the error
        #the error is how much you need to turn
        robot.drive(-speed, error*2)
        #turning
    robot.stop(Stop.BRAKE)
    #stop

def MoveMotor(degrees,speed,back):
    #move medium motor
    amotor.run_angle(speed, degrees, Stop.BRAKE)
    if back:
        #When the motor goes back to the starting position
        #for crane mission
        amotor.run_angle(-speed, degrees, Stop.BRAKE)

def TankTurnTo(direction, speed):
    CurrentGyro = gyro.angle()
    #Turns one wheel one way and the other wheel the other way
    if CurrentGyro - direction < 0:
        TankTurnRight(direction - CurrentGyro, speed)
    else:
        TankTurnLeft(CurrentGyro - direction, speed)
    RealStop()

def TankTurnLeft(degree, speed):
    CurrentDegrees = gyro.angle()
    #Turns one wheel one way and the other wheel the other way
    left.run(-speed)
    right.run(speed)
    stopDegree = CurrentDegrees - degree
    while (gyro.angle() > stopDegree):
        if abs(gyro.angle() - stopDegree) < 20:
            left.run(-80)
            right.run(80)
    robot.stop(Stop.BRAKE)

def TankTurnRight(degree, speed):
    CurrentDegrees = gyro.angle()
    #Turns one wheel one way and the other wheel the other way
    right.run(-speed)
    left.run(speed)
    stopDegree = CurrentDegrees + degree
    while (gyro.angle() < stopDegree):
        if abs(gyro.angle() - stopDegree) < 20:
            right.run(-80)
            left.run(80)
    robot.stop(Stop.BRAKE)

def RealStop():
    #Stops the motors twice for GOOD! Makes it more accurate
    #without the wheels somethimes still moving
    robot.stop(Stop.BRAKE)
    wait(10)
    robot.stop(Stop.BRAKE)

#We needed this stop because the lego EV3 stop function
#will sometimes keep one wheel moving when it stops


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
    mm = inch * 25.4
    #converts inches to millimeters
    rotation =  math.pi * wheel_diameter
    #circumference
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
        #Color reflect = reflection from color sensor
        error = ColorReflect - 40
        #40 is in the middle of black and white, where you want to go
        #the error is how much you need to turn
        robot.drive(speed,error * 0.5)
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
        robot.drive(speed,error)
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
        pass
    robot.stop(Stop.BRAKE)

def TurnTo(direction,speed):
    CurrentGyro = gyro.angle()
    if CurrentGyro - direction < 0:
        TurnRight(direction - CurrentGyro, speed)
    else:
        TurnLeft(CurrentGyro - direction, speed)



#Makes the robot turn right
def TurnRight(degree, speed):
    CurrentDegrees = gyro.angle()
    right.stop(Stop.BRAKE)
    left.run(speed)
    stopDegree = CurrentDegrees + degree
    while (gyro.angle() < stopDegree):
        pass
    robot.stop(Stop.BRAKE)


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
        robot.drive(-speed, error)
        #turning
    robot.stop(Stop.BRAKE)
    #stop

def MoveMotor(degrees,speed,back):
    amotor.run_angle(speed, degrees, Stop.BRAKE)
    if back:
        amotor.run_angle(-speed, degrees, Stop.BRAKE)


def TankTurnTo(direction, speed):
    CurrentGyro = gyro.angle()
    if CurrentGyro - direction < 0:
        TankTurnRight(direction - CurrentGyro, speed)
    else:
        TankTurnLeft(CurrentGyro - direction, speed)

def TankTurnLeft(degree, speed):
    CurrentDegrees = gyro.angle()
    left.run(-speed)
    right.run(speed)
    stopDegree = CurrentDegrees - degree
    while (gyro.angle() > stopDegree):
        pass
    robot.stop(Stop.BRAKE)

def TankTurnRight(degree, speed):
    CurrentDegrees = gyro.angle()
    right.run(-speed)
    left.run(speed)
    stopDegree = CurrentDegrees + degree
    while (gyro.angle() < stopDegree):
        pass
    robot.stop(Stop.BRAKE)

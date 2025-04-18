from adafruit_motorkit import MotorKit
kit = MotorKit()
from time import sleep
from pprint import pprint as pp

s=0.6

forward = [s, s, s, s]
backward = [-s, -s, -s, -s]
clockwise  = [s, s, -s, -s]
counterclockwise = [-s, -s, s, s]
right = [-s, s, -s, s]
left = [s, -s, s, -s]
ten = [s, 0, s, 0]
two = [0, s, 0, s]
four = [-s, 0, -s, 0]
eight = [0, -s, 0, -s]
stop = [0, 0, 0, 0]
roundclockwise = [0, 0, s, s]
spinclockwise = [-s, 0, 0, s]

def drive(command, kit):
  pp(command)
  kit.motor1.throttle = command[0]
  kit.motor2.throttle = command[1]
  kit.motor3.throttle = command[2]
  kit.motor4.throttle = command[3]

duration = 1
drive(forward, kit)
sleep(duration)
drive(backward, kit)
sleep(duration)
drive(clockwise, kit)
sleep(duration)
drive(counterclockwise, kit)
sleep(duration)
drive(right, kit)
sleep(duration)
drive(left, kit)
sleep(duration)
drive(two, kit)
sleep(duration)
drive(four, kit)
sleep(duration)
drive(roundclockwise, kit)
sleep(duration)
drive(spinclockwise, kit)
sleep(duration)
drive(stop, kit)

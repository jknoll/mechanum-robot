from adafruit_motorkit import MotorKit
kit = MotorKit()

stop = [0, 0, 0, 0]


def drive(command, kit):
  pp(command)
  kit.motor1.throttle = command[0]
  kit.motor2.throttle = command[1]
  kit.motor3.throttle = command[2]
  kit.motor4.throttle = command[3]

drive(stop, kit)

from adafruit_motorkit import MotorKit
from pprint import pprint as pp
import curses

kit = MotorKit()

forward = [1, 1, 1, 1]
backward = [-1, -1, -1, -1]
clockwise  = [1, 1, -1, -1]
counterclockwise = [-1, -1, 1, 1]
right = [-1, 1, -1, 1]
left = [1, -1, 1, -1]
ten = [1, 0, 1, 0]
two = [0, 1, 0, 1]
four = [-1, 0, -1, 0]
eight = [0, -1, 0, -1]
stop = [0, 0, 0, 0]
roundclockwise = [0, 0, 1, 1]
spinclockwise = [-1, 0, 0, 1]

def drive(command, kit):
  kit.motor1.throttle = command[0]
  kit.motor2.throttle = command[1]
  kit.motor3.throttle = command[2]
  kit.motor4.throttle = command[3]

def main(stdscr):
    # do not wait for input when calling getch
    # stdscr.nodelay(1)

    curses.halfdelay(2) # delay before repolling in tenths of a second
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        print(c)
        if c != -1:
            # print numeric value
            stdscr.addstr(str(c) + ' ')
            stdscr.refresh()
            # return curser to start position
            stdscr.move(0, 0)
            if 119 == c:
                drive(forward, kit)
            if 115 == c:
                drive(backward, kit)
            if 97 == c:
                drive(clockwise, kit)
            if 100 == c:
                drive(counterclockwise, kit)
            if 113 == c:
                drive(left, kit)
            if 101 == c:
                drive(right, kit)
        else:
            drive(stop, kit)

if __name__ == '__main__':
    curses.wrapper(main)

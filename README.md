# mechanum-robot
Control system for simple mechanum-wheeled holonomic drive Raspberry Pi based robot.

## Parts List
- Raspberry Pi 4B
- Mini SD Card
- 2 x Left & Right Mecanum Wheel Pair - 48mm Diameter (TT Motor or Cross Axle (2-pack)) [ID:4990]
- 1 x Adafruit DC & Stepper Motor Bonnet for Raspberry Pi [ID:4280]
- 4 x DC Gearbox Motor - "TT Motor" - 200RPM - 3 to 6VDC [ID:3777]
- 4xAA battery power pack and 4xAA batteries to power the DC & Stepper Motor Bonnet
- USB cell phone charger to provide mobile power to the RaspPi
- Micro speaker for audio out
- Raspberry Pi Camera
- Assorted legos for chassis


## Setup
Build the robot. Ensure that the Mechanum wheels are assigned to the four corners of the chassis such that the subwheels form an "x".

Clone this repo:

``` bash
git clone git@github.com:jknoll/mechanum-robot.git
```

Create a virtualenv and activate it:

```bash
$ python -m venv .mechanum-robot
$ source .mechanum-robot/bin/activate
```

Install dependencies:
```bash
$ pip install -r requirements.txt`
```

Ensure that I2C is enabled:
```bash
sudo raspi-config # turn on I2C
```

## Usage
To test basic control of a single motor:
```bash
python3 motor_test.py`
```

To run a mechanum wheel test pattern:
```bash
python3 robot_keyboardless.py3`
```
To kill motors mid-action (be ready with this command on early runs):
```bash
python3 kill.py3
```

To view webcam:
```bash
python3 stream.py3 & # then go to [robot IP address:8000] to view the webcam
```


## Bugs/Todos
Webcam doesn't seem to work with picamera and a 64 bit OS. Perhaps with picamera2 or some other library.

Keyboard control can be made to work, but the `keyboard` library must be run as root, with the dependencies installed within the root account. Looking at alternatives, or perhaps leapfrogging directly to xbox controller control.



`/audio/*.wav` files are for testing audio playback





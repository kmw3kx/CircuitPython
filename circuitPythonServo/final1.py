# circuitPythonServo
# Borrowed from: https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/circuitpython-servo
# https://github.com/jkammau97/CircuitPython
import time
import board
import digitalio
import pulseio
from adafruit_motor import servo
import touchio
# servo pin is A2
# green wire is A0
# yellow wire is A1
# green led is D1
# yellow led is D0

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
# add LED's
ledG = digitalio.DigitalInOut(board.D1)
ledG.direction = digitalio.Direction.OUTPUT
ledY = digitalio.DigitalInOut(board.D0)
ledY.direction = digitalio.Direction.OUTPUT

#set servo bounds

maxAngle = 160
minAngle = 20
direction = None
my_servo.angle = 90
pastGreen = None
pastYellow = None
angleChange = 20

# Add in all of the capacitive touch stuff

touch_pad_green = board.A0  # Will not work for Circuit Playground Express!
touch_pad_yellow = board.A1
# touch_pad = board.A1  # For Circuit Playground Express

touchGreen = touchio.TouchIn(touch_pad_green)
touchYellow = touchio.TouchIn(touch_pad_yellow)

while True:
    ledG.value = touchGreen.value
    ledY.value = touchYellow.value
    if touchGreen.value and not(pastGreen):
        print("Touched Green!")
        direction = True
    if touchYellow.value and not(pastYellow):
        print("Touched Yellow!")
        direction = False
# for direction, true = right and yellow; false = left and green
    if direction and my_servo.angle < maxAngle:
        my_servo.angle = my_servo.angle + angleChange
    if not(direction) and my_servo.angle > minAngle:
        my_servo.angle = my_servo.angle - angleChange
    pastYellow = touchYellow.value
    pastGreen = touchGreen.value
    time.sleep(.01)
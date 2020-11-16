# circuitPythonServo
# Borrowed from: https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/circuitpython-servo
# https://github.com/jkammau97/CircuitPython
import time
import board
import pulseio
from adafruit_motor import servo
import touchio

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

#set servo bounds

maxAngle = 160
minAngle = 20

# Add in all of the capacitive touch stuff

touch_pad_green = board.A0  # Will not work for Circuit Playground Express!
touch_pad_yellow = board.A1
# touch_pad = board.A1  # For Circuit Playground Express

touchGreen = touchio.TouchIn(touch_pad_green)
touchYellow = touchio.TouchIn(touch_pad_yellow)

while True:
    if touchGreen.value and not(pastGreen):
        print("Touched Green!")
        direction = true
        pastGreen = touchGreen.value
    if touchYellow.value and not(pastYellow):
        print("Touched Yellow!")
        direction = false
        pastYellow = touchYellow.value
# for direction, true = right and yellow; false = left and green
    if direction and angle:

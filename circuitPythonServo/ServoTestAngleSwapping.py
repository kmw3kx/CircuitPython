# circuitPythonServo
# Borrowed from: https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/circuitpython-servo
# https://github.com/jkammau97/CircuitPython
import time
import board
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    my_servo.angle = 0
    time.sleep(.5)
    my_servo.angle = 10
    time.sleep(1)
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
    for angle in range(30, 150, 5):  # 0 - 180 degrees, 10 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.01)
    time.sleep(.5)
    for angle in range(150, 30, -5): # 180 - 0 degrees, 10 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.01)
    time.sleep(.5)
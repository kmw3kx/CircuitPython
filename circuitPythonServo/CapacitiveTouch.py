# Capacitive Touch Code
# From: https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/circuitpython-cap-touch
#
import time

import board
import touchio

touch_pad_green = board.A0  # Will not work for Circuit Playground Express!
touch_pad_yellow = board.A1
# touch_pad = board.A1  # For Circuit Playground Express

touchGreen = touchio.TouchIn(touch_pad_green)
touchYellow = touchio.TouchIn(touch_pad_yellow)

while True:
    if touchGreen.value and not(pastGreen):
        print("Touched Green!")
    if touchYellow.value and not(pastYellow):
        print("Touched Yellow!")
    pastGreen = touchGreen.value
    pastYellow = touchYellow.value
    time.sleep(0.05)
# PWM Object
# Borrowed from: https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/circuitpython-pwm
# Edited by Bob Kammauff
# https://github.com/jkammau97/CircuitPython
import time
import board
import pulseio

led = pulseio.PWMOut(board.D5, frequency=5000, duty_cycle=0)

while True:
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(0.01)
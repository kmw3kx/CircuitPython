# circuitPythonPhotointerrupters
# Bob K.
# https://github.com/jkammau97/CircuitPython

import time

import digitalio
import board
photoPin = digitalio.DigitalInOut(board.D5)
photoPin.direction = digitalio.Direction.INPUT
photoPin.pull = digitalio.Pull.UP

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

lcd.set_cursor_pos(0, 0)
lcd.print("The number of interrupts is ")

init = time.monotonic()

count = 0
pastInterrupt = False
#returns amount of time elapsed since the program started in SECONDS
while True:
    interrupted = photoPin.value
    now = time.monotonic()
    if interrupted and not(pastInterrupt):
        count = count + 1
        print("interrupt")
    pastInterrupt = interrupted

    if now - init > 4:  # If 4 seconds elapses
        lcd.set_cursor_pos(1, 12)
        lcd.print("    ")
        lcd.set_cursor_pos(1, 12)
        lcd.print(str(count))
        # printing like this allows us to only update the text on the lcd that is changing, reducing flicker
        init = now
        print(now)


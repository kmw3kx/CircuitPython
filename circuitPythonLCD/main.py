# Bob Kammauff
# circuitPythonLCD
# https://github.com/jkammau97/CircuitPython
# code from https://cvilleschools.instructure.com/courses/31071/assignments/303469
import time
# for time
import board
# for pin references
# for digital pins
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import touchio
# for capacitive touch
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

# add in a counter
count = 0
increment = 1
# can be 1 or -1
# Add in all of the capacitive touch stuff
touch_pad_green = board.A0  # Will not work for Circuit Playground Express!
touch_pad_yellow = board.A1
touchGreen = touchio.TouchIn(touch_pad_green)
touchYellow = touchio.TouchIn(touch_pad_yellow)

# green will be the counter
# yellow will be the switch

# and the variables for the past values
pastGreen = None
pastYellow = None

lcd.set_cursor_pos(0, 0)
lcd.print("Increment ")

lcd.set_cursor_pos(1,0)
lcd.print("Value ")

while True:
    if touchYellow.value and not(pastYellow):
        print("Touched Yellow!")
        increment = increment*-1
        lcd.set_cursor_pos(0, 10)
        lcd.print(str(increment) + " ")
        print(increment)

    if touchGreen.value and not(pastGreen):
        print("Touched Green!")
        count = count + increment
        lcd.set_cursor_pos(1, 6)
        lcd.print("          ")
        # print 10 spaces to clear the past number
        lcd.set_cursor_pos(1, 6)
        lcd.print(str(count))
        print(count)
    pastYellow = touchYellow.value
    pastGreen = touchGreen.value
    time.sleep(.01)
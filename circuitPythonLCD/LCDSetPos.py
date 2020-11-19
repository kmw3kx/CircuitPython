# Bob Kammauff
# circuitPythonLCD
# https://github.com/jkammau97/CircuitPython
# code from https://cvilleschools.instructure.com/courses/31071/assignments/303469
import time
# for time
import board
# for pin references
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

lcd.print("Hello, Engineer!")
time.sleep(1)
lcd.clear()

while True:
    lcd.set_cursor_pos(0,0)
    lcd.print("Hi")
    time.sleep(1)
    lcd.clear()
    lcd.set_cursor_pos(1,0)
    lcd.print("Bob")
    time.sleep(1)
    lcd.clear()

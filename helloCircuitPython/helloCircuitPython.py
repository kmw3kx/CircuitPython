# helloCircuitPython
# Bob Kammauff
# 10/21/2020
import board
import time
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)



while True:
     dot.fill((5,0,0))
     print("RED")
     time.sleep(0.5)
     dot.fill((0,5,10))
     print("Cyan")
     time.sleep(0.5)
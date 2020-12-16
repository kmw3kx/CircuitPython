import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

measurement = None
listOfDist = []
# declares list w/out any values in it

count = 5 # the max amount of numbers I wanna put in my list

while True:
    listOfDist.clear()
    for x in range(count)
	    try:
            listOfDist.append(sonar.distance)
            print(str(x))
        except RuntimeError:
            print("Runtime")
            continue
            # what continue does is just moves on to the
            # next reading
        time.sleep(.01)
    listOfDist.sort()
    mid = len(listOfDist) // 2
    # // means floor division
    medDist = (listOfDist[mid] + listOfDist[~mid]) / 2
    print(listOfDist)
    print(str(medDist))
    time.sleep(1)

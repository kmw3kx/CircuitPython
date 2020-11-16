# CircuitPython
My circuit python assignments

https://learn.adafruit.com/welcome-to-circuitpython

https://www.markdownguide.org/cheat-sheet/


> blockquote

`In-line Code`

```python
code block here

while True:
     dot.fill((5,0,0))
     print("RED")
     time.sleep(0.5)
     dot.fill((0,5,10))
     print("Cyan")
     time.sleep(0.5)
```
## Getting Started
Go to the link above and click the green buttons at the end of the first text box. Read through the tutorial to learn how to boot the Metro 0 and turn it into a F:CIRCUITPY drive

Once it's like that, you need to save ur code file as `code.py` to the board. In order to update the file on Github, put each assignment in github in it's own folder with the file name. 

Ok i need to install lib

search for the `neopixel.mpy`and add it into the lib folder on the metro express.

alrighty I think that's all I need to do. Let's get started w/ the coding! 

## Table of Contents
[Table of Contents](#Table-of-Contents)

* [helloCircuitPython](#helloCircuitPython)
  * [Description](#description)
  * [Process](#Process)
  * [Evidence](#Evidence)
  * [Reflection](#Reflection)
* [circuitPythonServo](#circuitPythonServo)
  * [Description](#Description-1)
  * [Process](#Process-1)
  * [Evidence](#Evidence-1)
  * [Reflection](#Reflection-1)


## helloCircuitPython
*[Table of Contents](#Table-of-Contents)*

 * [Description](#description)
 * [Process](#Process)
 * [Evidence](#Evidence)
 * [Reflection](#Reflection)

### Description



### Process


### Evidence



### Reflection



---


## circuitPythonServo
*[Table of Contents](#Table-of-Contents)*

  * [Description](#description-1)
  * [Process](#Process-1)
  * [Evidence](#Evidence-1)
  * [Reflection](#Reflection-1)
### Description

Now it's time to control a servo with a circuit python

[The Assignment Page](https://cvilleschools.instructure.com/courses/31071/assignments/300471?module_item_id=1016569)

>Last year, whether you knew it or not, when you were sending signals to servos to make them move, you were using PWM, or Pulse Width Modulation.  With PWM, you encode information by modulating the width of a electronic pulse.  In other words, you  send a bunch of pulses to your servo and the width of those pulses is what the servo interprets as a message.
>In CircuitPython, when you make a PWM object, you specify the duty cycle (which can be changed) and frequency.  Frequency is just how often the pulses occur.  Notice in the picture above that all of the square pulses start at the same time, meaning they have the same frequency.  Duty cycle determines how long the pulses stay high.  In CircuitPython, the duty cycle is a number between 0, which is 0% and 216 (65,536), which is 100%.

This all means absolutely noting to y'all tho (yet), so I'll jump to the assignment description

>Get a 180° micro servo to slowly sweep back and forth between 0 and 180°.
>
>The spicy part (FYI: "spicy" means "fun", "extra spicy" means "really fun, but optional") : stick two random wires into two of the Analog In pins on your Metro.  Use those two wires and the magic of capacitive touch to control the servo.  Touch one wire and the servo goes one way.  Touch the other wire and it goes the other way.  The servo only moves if you're touching a wire.
>
>I don't expect you know know how to program capacitive touch on your Metro.  That's what Google is for.  But please don't Google "how to make a servo move using capacitive touch."  I hope you will improve your Google-fu in this class.  Break down what you need to know.  Maybe start with "Metro express capacitive touch" , or "CircuitPython capacitive touch" or something like that.
>
>When you're done, upload your code, document your work in your repo README, and submit your repo URL.  Additionally, you should upload a short video to Canvas, showing the thing working.  Use the record option when submitting, it's really easy. 

Big Hint:

>Make sure you have downloaded the appropriate [Adafruit CircuitPython library bundle.](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/)  So, if you're running version 5.x of CircuitPython, grab the 5.x bundle.  Inside the bundle, you'll find a "lib" folder and inside that you'll find an "adafruit_motor" folder.  Inside that, you'll find the "servo.mpy" library.  Copy that file to the lib folder on your Metro and you can use Adafruit's amazing servo object!  In other words, you can say stuff like `myServo.angle = 90` instead of having to figure out PWM communication.

### Process

Ok, so first off, I'm gonna approach it like how I would an Arduino:

1. I need to figure out how to 'attach' the servo to a pin
2. How to write a value to the pin

Python is an object-based programming language, so I just have to make an object and connect that to the pin.

Basically, my first question is how do I tell it which pin to use?

Ok, so for this one, the `d` next to the number means it's a digital pin



So, I'm a bit off-topic now, but I think I can just start with an LED, and it'll work with the servo

Here's some code that I stole from [Adafruit.](https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/circuitpython-pwm)

```python
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
```

It's quite cool what they are doing here. The pin actually cannot be truly analog, so they use PWM to make it appear analog. 

Let's see what it looks like on the Metro:

[<img src="circuitPythonServo/PWMTestWLED.GIF" alt="PWMTestWLED.GIF" width="350" height="250">](circuitPythonServo/PWMTestWLED.GIF)

Sick gif dude

I think it'll just work if I now plug in the servo

Actually, I'm gonna slow down the cycle speed first



Ok and so it doesn't work. Let's try something else

So we're going somewhere else entirely! [Here's the rad Adafruit page I found.](https://learn.adafruit.com/adafruit-metro-m0-express-designed-for-circuitpython/circuitpython-servo)

And here's the code they're giving me to upload:

```python
import time
import board
import pulseio
from adafruit_motor import servo
 
# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
 
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
 
while True:
    for angle in range(0, 180, 5):  
        # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):
        # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
```

Wow, look at those `for` loops. They are very simple. So how it works, I'm guessing, is that the for loop starts the variable `angle` at 0, then increments up by 5 and writes that to the angle portion of the `my_servo` object, so it actually knows what to do with that number. Huh ok then. Well let's run it on the metro then.

ins link to video of it sweeping

My servo is quite shaky, let me try and just have it change positions

```python
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
```

Ok so it's a problem with the code because that worked perfectly 

Let's make it go faster and pause at the end.

After messing with some variables, the settings that ended up working the best were the time.sleep being .01 and the angle being 5



### Evidence

### Reflection

---

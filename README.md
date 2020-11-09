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
  * [Evidence](#Evidence)
  * [Image](#Image)
  * [Reflection](#Reflection)
* [circuitPythonServo](#circuitPythonServo)
  * [Description](#Description-1)
  * [Evidence](#Evidence-1)
  * [Image](#Image-1)
  * [Reflection](#Reflection-1)
* [Fork](#Fork)
  * [Description](#Description-2)
  * [Evidence](#Evidence-2)
  * [Image](#Image-2)
  * [Reflection](#Reflection-2)
* [Tire](#Tire)
  * [Description](#Description-3)
  * [Evidence](#Evidence-3)
  * [Image](#Image-3)
  * [Reflection](#Reflection-3)
* [Wheel](#Wheel)
  * [Description](#Description-4)
  * [Evidence](#Evidence-4)
  * [Image](#Image-4)
  * [Reflection](#Reflection-4)
* [AxleCollarBearings](#AxleCollarBearings)
  * [Description](#Description-5)
  * [Evidence](#Evidence-5)
  * [Image](#Image-5)
  * [Reflection](#Reflection-5)

## helloCircuitPython
*[Table of Contents](#Table-of-Contents)*

 * [Description](#description)
 * [Evidence](#Evidence)
 * [Image](#Image)
 * [Reflection](#Reflection)

### Description



### Evidence


### Image



### Reflection



---


## circuitPythonServo
*[Table of Contents](#Table-of-Contents)*

  * [Description](#description-1)
  * [Evidence](#Evidence-1)
  * [Image](#Image-1)
  * [Reflection](#Reflection-1)
### Description

Now it's time to control a servo with a circuit python

[The Assignment Page](https://cvilleschools.instructure.com/courses/31071/assignments/300471?module_item_id=1016569)

>Last year, whether you knew it or not, when you were sending signals to servos to make them move, you were using PWM, or Pulse Width Modulation.  With PWM, you encode information by modulating the width of a electronic pulse.  In other words, you  send a bunch of pulses to your servo and the width of those pulses is what the servo interprets as a message.
>In CircuitPython, when you make a PWM object, you specify the duty cycle (which can be changed) and frequency.  Frequency is just how often the pulses occur.  Notice in the picture above that all of the square pulses start at the same time, meaning they have the same frequency.  Duty cycle determines how long the pulses stay high.  In CircuitPython, the duty cycle is a number between 0, which is 0% and 216 (65,536), which is 100%.

This all means absolutely noting to y'all tho, so I'll jump to the assignment description

>Get a 180° micro servo to slowly sweep back and forth between 0 and 180°.
>
>The spicy part (FYI: "spicy" means "fun", "extra spicy" means "really fun, but optional") : stick two random wires into two of the Analog In pins on your Metro.  Use those two wires and the magic of capacitive touch to control the servo.  Touch one wire and the servo goes one way.  Touch the other wire and it goes the other way.  The servo only moves if you're touching a wire.
>
>I don't expect you know know how to program capacitive touch on your Metro.  That's what Google is for.  But please don't Google "how to make a servo move using capacitive touch."  I hope you will improve your Google-fu in this class.  Break down what you need to know.  Maybe start with "Metro express capacitive touch" , or "CircuitPython capacitive touch" or something like that.
>
>When you're done, upload your code, document your work in your repo README, and submit your repo URL.  Additionally, you should upload a short video to Canvas, showing the thing working.  Use the record option when submitting, it's really easy. 

Big Hint:

>Make sure you have downloaded the appropriate [Adafruit CircuitPython library bundle.](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/)  So, if you're running version 5.x of CircuitPython, grab the 5.x bundle.  Inside the bundle, you'll find a "lib" folder and inside that you'll find an "adafruit_motor" folder.  Inside that, you'll find the "servo.mpy" library.  Copy that file to the lib folder on your Metro and you can use Adafruit's amazing servo object!  In other words, you can say stuff like `myServo.angle = 90` instead of having to figure out PWM communication.

### Evidence

### Image

### Reflection

---


## Fork
*[Table of Contents](#Table-of-Contents)*
  * [Description](#Description-2)
  * [Evidence](#Evidence-2)
  * [Image](#Image-2)
  * [Reflection](#Reflection-2)
### Description

### Evidence

### Image

### Reflection

---


## Tire
*[Table of Contents](#Table-of-Contents)*
  * [Description](#Description-3)
  * [Evidence](#Evidence-3)
  * [Image](#Image-3)
  * [Reflection](#Reflection-3)
### Description

### Evidence

### Image

### Reflection

---


## Wheel
*[Table of Contents](#Table-of-Contents)*
### Description

### Evidence

### Image

### Reflection

---
*[Table of Contents](#Table-of-Contents)*

## AxleCollarBearings

### Description

### Evidence

### Image

### Reflection

---
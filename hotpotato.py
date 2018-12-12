import radio
import random
from microbit import *

radio.on()

potato = -1

while True:
    if button_a.is_pressed():
        potato = random.randint(10, 20)
        break
      
while True:  
    incoming = radio.receive()
    if incoming is not None:
        potato = int(incoming)
  
    if potato == 0:
        display.show(Image.SKULL)
    
    elif potato > 0:
        if accelerometer.was_gesture("shake"):
            potato = potato -1
            radio.send(str(potato))
            potato = -1
  
    elif potato == -1:
        display.show(Image.HAPPY)

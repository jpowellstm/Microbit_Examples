""" A basic examples to demonstrate how the micro:bits can communicate with each other
"""

import radio
from microbit import *

radio.on()

while True:
    if button_a.was_pressed():
        radio.send('hello') 
   
    incoming = radio.receive()
 
    if incoming is not None:   
        display.scroll(incoming)
    

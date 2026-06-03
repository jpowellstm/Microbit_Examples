"""Communication with channel and power settings
"""

import radio
from microbit import *

radio.on()
radio.config(channel=19)
radio.config(power=7)

while True:
    if button_a.was_pressed():
        radio.send('hello') 
   
    incoming = radio.receive()
    if incoming == 'hello':
        sleep(500)
        radio.send('world')

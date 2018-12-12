# Change the image on the screen based o a different gesture

from microbit import *

while True:
    if accelerometer.was_gesture("shake"):
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)

display.clear()

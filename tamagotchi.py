# An example of a very basic tamagotchi 

from microbit import *

count = 0 
fed = 0

while True:
    display.show(Image.SAD)
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        fed = fed + 1
        sleep(5000)    
    elif button_b.is_pressed():
        count = count + 1
        display.scroll("ow")
    elif count > 10:
        display.scroll("DEAD")
    elif fed > 5:
        display.scroll("bluuh")
        fed = 0
    elif accelerometer.was_gesture("shake"):
        display.scroll("arrgg")
        count = count + 2

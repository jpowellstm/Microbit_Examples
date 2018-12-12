# Examples of event loops

# Example 1 - a very basic loop that displays an image for 10 seconds then changes

from microbit import *

while running_time() < 10000:
    display.show(Image.ASLEEP)

display.show(Image.SURPRISED)

# Example 2 - displays an image if button a is pressed and ends if button b is pressed

from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        break
    else:
        display.show(Image.SAD)

display.clear()

from microbit import *
import neopixel

def neo_init(size):
  """initialise neopixel library and set colours
  """
  global np
  global colours
  np = neopixel.NeoPixel(pin0, size**3)

  # define a dictionary of colours using RGB values. More can be added by
  using an online colour picker.

  colours = {
  'purple': (40, 0, 40),
  'red': (255 , 0, 0),
  'green': (0, 255, 0),
  'blue': (0, 0, 255),
  }
  
def map(x,y,z, size):
  """Convert from the x,y,z coordinate system to the value required by the neopixel library
  """
        
        q = 0
        if z % 2 == 0:
            if y % 2 == 0:
                q = (y * size) + x
            else:
                q = (y * size) + size - 1 - x
        else:
            if size % 2 == 0:
                y = size - y - 1
            else:
                if x % 2 == 0:
                    q = (size * (size - x)) - 1 - y
                else:
                    q = ((size - 1 - x) * size) + y
        return (z * size * size) + q
      
def setxyz(x, y, z, colour, size):
  """
  lights an LED a given colour using a cartesian coordinate system.
  size should be 3 for a 3x3x3 cube
  """
        neo_num = map(x, y, z, size)        
        np[neo_num] = colours[colour]
  
"""Example 1
Light a single LED red.
"""

neo_init(3)
setxyz(1,1,1,'red', 3)
np.show()

"""Example 2
Loop over all the LED's in the array
"""

neo_init(3)

for x in range(3):
  for y in range(3):
    for z i range(3):
      setxyz(x,y,z,'red', 3)
      np.show()

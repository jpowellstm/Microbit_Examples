from microbit import *
import neopixel

def neo_init(size):
# initialise neopixel library and set colours
  global np
  global colours
  np = neopixel.NeoPixel(pin0, size**3)
  
  colours = {
  'purple': (40, 0, 40),
  'red': (255 , 0, 0),
  'green': (0, 255, 0),
  'blue': (0, 0, 255),
  }
  
def map(x,y,z, size):
        
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
        neo_num = map(x, y, z, size)        
        np[neo_num] = colours[colour]
      
neo_init(3)
setxyz(1,1,1,'red', 3)
np.show()

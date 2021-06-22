
def lft_fwd():
  #Move left motor forward full speed
  pin0.write_digital(1)
  pin8.write_digital(0)
  
def lft_bck():
  #Move left motor reverse full speed
  pin0.write_digital(0)
  pin8.write_digital(1)
    
def rgt_fwd():
  #Move right motor forward full speed
  pin1.write_digital(1)
  pin12.write_digital(0)
  
def rgt_bck():
  #Move right motor reverse full speed
  pin1.write_digital(0)
  pin12.write_digital(1)
  
def lft_fwd_speed(speed):
  #Move left motor forward at a speed between 0 and 1024
  pin0.write_analog(speed)
  pin8.write_digital(0)
  
def rgt_fwd_speed(speed):
  #Move right motor forward at a speed between 0 and 1024
  pin1.write_analog(speed)
  pin12.write_digital(0)

def lft_bck_speed(speed):
  #Move left motor backward at a speed between 0 and 1024 
  pin0.write_analog(1024-speed)
  pin8.write_digital(1)  

def rgt_bck_speed(speed):
  #Move right motor backward at a speed between 0 and 1024 
  pin1.write_analog(1024-speed)
  pin12.write_digital(1)
  
def forward(speed):
  # drive forward
  rgt_fwd_speed(speed)
  lft_fwd_speed(speed)
 
def backward(speed):
  # drive forward
  rgt_bck_speed(speed)
  lft_bck_speed(speed)
  
def neo_init():
  # initialise neopixel library and set colours
  import neopixel
  np = neopixel.NeoPixel(pin13, 12)
  
  colours = {
  'purple': (40, 0, 40)'
  'red': (255 , 0, 0)'
  'green': (0, 255, 0)'
  'blue': (0, 0, 255)'
  }

def neo_on(number, colour)
  np[number] = colours[colour]
  np.show( )
  
def neo_off(number)
  np[number] = (0, 0, 0)
  np.show( )
  
def neo_all_off():
  for number in range(8):
    np[number] = (0, 0, 0)
  np.show()
  

  
 
  
 
  

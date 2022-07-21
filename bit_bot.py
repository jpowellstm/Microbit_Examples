
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
  pin0.write_analog(speed)
  pin8.write_digital(1)  

def rgt_bck_speed(speed):
  #Move right motor backward at a speed between 0 and 1024 
  pin1.write_analog(speed)
  pin12.write_digital(1)
  
def forward(speed):
  # drive forward
  rgt_fwd_speed(speed)
  lft_fwd_speed(speed)
 
def backward(speed):
  # drive backward
  rgt_bck_speed(speed)
  lft_bck_speed(speed)
  
def stop():
   pin0.write_digital(0)
   pin8.write_digital(0)
   pin1.write_digital(0)
   pin12.write_digital(0)
  
def turn(direction, angle):
  # Direction given as 'left' or 'right'
  # Angle between 0 and 90 degrees
  
  angle = round(angle/90 * 1023)
  
  if direction == 'left':
    rgt_fwd_speed(angle)
    lft_bck_speed(angle)
  else:
    lft_fwd_speed(angle)
    rgt_bck_speed(angle)
  
  sleep(500) # this might need tweaking to get the right angle
  stop()
  
def follow_line():
  # Follow a black line on a white background
  
   lft = pin16.read_digital()
   rgt = pin14.read_digital()
  
   if lft==0 and rgt==1:
       turn('right', 45)
   elif lft==1 and rgt==0:
       turn('left', 45)
   elif rgt==1 and lft==1:
       forward(400)
   sleep(20)

def neo_init():
# initialise neopixel library and set colours
  import neopixel
  global np
  global colours
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
  
def ultra_init():
  from machine import time_pulse_us
  global trig
  global echo
  trig = pin15
  echo = pin1
  trig.write_digital(0)
  echo.read_digital()
  
  
def get_distance():
    trig.write_digital(1)
    trig.read_digital(0)
    micros = time_pulse_us(echo, 1)
    t_echo = micros/1000000
    dist_cm = (t_echo / 2) *34300
    sleep(100)
    return dist_cm
  

  
 
  
 
  

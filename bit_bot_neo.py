"""
This file adds functionality to use the neopixel LEDs at the front of the robot.
"""

from microbit import *
from machine import time_pulse_us

def lft_fwd_speed(speed):
  # Move left motor forward at a speed between 0 and 1024
  pin0.write_analog(speed)
  pin8.write_digital(0)
  
def rgt_fwd_speed(speed):
  # Move right motor forward at a speed between 0 and 1024
  pin1.write_analog(speed)
  pin12.write_digital(0)

def forward(speed):
  # drive forward
  rgt_fwd_speed(speed)
  lft_fwd_speed(speed)

def stop():
  # Stop both motors
   pin0.write_digital(0)
   pin8.write_digital(0)
   pin1.write_digital(0)
   pin12.write_digital(0)

def turn(direction, angle):
  # Direction given as 'left' or 'right'
  # Angle between 0 and 90 degrees
  # The amount of sleep time at the end of the function needs tweaking to get the angle right
  
  angle = round(angle/90 * 1023)
  
  if direction == 'left':
    rgt_fwd_speed(angle)
    lft_bck_speed(angle)
  else:
    lft_fwd_speed(angle)
    rgt_bck_speed(angle)
  
  sleep(50) # this might need tweaking to get the right angle
  stop()

def neo_init():
# initialise neopixel library and set colours, if you want to add more colours define them below
  import neopixel
  global np
  global colours
  np = neopixel.NeoPixel(pin13, 8)
  
  colours = {
  'purple': (40, 0, 40),
  'red': (255 , 0, 0),
  'green': (0, 255, 0),
  'blue': (0, 0, 255),
  }

def neo_on(number, colour):
  # takes the number of the neopixel to turn on and the colour as inputs
  np[number] = colours[colour]
  np.show( )
  
def neo_off(number):
  # Takes the number of the neopixel to turn off 
  np[number] = (0, 0, 0)
  np.show( )
  
def neo_all_off():
  # Turns off all neopixels
  for number in range(8):
    np[number] = (0, 0, 0)
  np.show()
  
def ultra_init():
  global trig
  trig = pin15
  trig.write_digital(0)
  
def get_distance():
    trig.write_digital(1)
    sleep_us(10)
    trig.write_digital(0)
    
    while trig.read_digital() == 0:
      pass
    
    micros = time_pulse_us(trig, 1)
    t_echo = micros/1000000
    dist_cm = (t_echo / 2) *34300
    sleep(100)
    return dist_cm

######################################################################################################  
# This is part of the programme that makes the robot move. Try changing some of the numbers to get it 
# different things
######################################################################################################

neo_init()
neo_on(1, 'red')
sleep(2000)
neo_all_off()

 
  
 
  

"""
This is a very basic maze navigator for a bit bot using ultrasound detection.
"""
from microbit import *
from machine import time_pulse_us
  
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
  """ Direction given as 'left' or 'right'
      Angle between 0 and 90 degrees
      The amount of sleep will need to be tweaked to get the angle right.
      
      Example use: turn('right', 45)
      
  """
  angle = round(angle/90 * 1023)
  
  if direction == 'left':
    rgt_fwd_speed(angle)
    lft_bck_speed(angle)
  else:
    lft_fwd_speed(angle)
    rgt_bck_speed(angle)
  
  sleep(500) # this might need tweaking to get the right angle
  stop()
  
def ultra_init():
  global trig
  trig = pin15
  trig.write_digital(0)
  
def get_distance():
    trig.write_digital(1)
    sleep(10)
    trig.write_digital(0)
    
    while trig.read_digital() == 0:
      pass
    
    micros = time_pulse_us(trig, 1)
    t_echo = micros/1000000
    dist_cm = (t_echo / 2) *34300
    sleep(100)
    return dist_cm
  
 # The main run loop follows

ultra_init()
while True:
  forward(512)
  if get_distance() < 20:
    stop()
    turn('right', 20)
    

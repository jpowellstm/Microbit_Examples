"""
If you download this to the microbit and turn the robot on it should drive forward until it detects an obstacle that is less that
50 cm in front of it and then stop. Try to make the following modifications

1. If the robot detects an obstact within 50 cm it should slow down. 
   It should stop if it detects an obstacle within 25 cm.
   
2. After stopping the robot should backup, turn through 90 degrees and then carry on forward.
   You will need to tweak the amount of sleep in the turn function to get it to the right angle.

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
    sleep_us(10)
    trig.write_digital(0)
    
    while trig.read_digital() == 0:
      pass
    
    micros = time_pulse_us(trig, 1)
    t_echo = micros/1000000
    dist_cm = (t_echo / 2) *34300
    sleep(100)
    return dist_cm
  
 # The main run loop follows
 while True:
  forward(512)
  if get_distance() < 50:
    stop()
    break

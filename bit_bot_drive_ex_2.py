"""
This file contains the most basic functions to get the bitBot to drive forward and turn
left and right. Go to the bottom of the file to see the part of the programme that m
akes it move.
"""

from microbit import *

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
  
  sleep(50) # this might need tweaking to get the right angle
  stop()

def forward(speed):
  # drive forward
  rgt_fwd_speed(speed)
  lft_fwd_speed(speed)
  

######################################################################################################  
# This is part of the programme that makes the robot move. Try changing some of the numbers to get it 
# different things
######################################################################################################
  
forward(600)
sleep(2000)
stop()
turn('left', 3)
forward(600)
sleep(2000)
stop()

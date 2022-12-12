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
  
def follow_line():
  # Follow a black line on a white background
  
   lft = pin16.read_digital()
   rgt = pin14.read_digital()
  
   if lft==1 and rgt==1:
       turn('left', 3)
   elif lft==0 and rgt==0:
       turn('right', 3)
   else:
       forward(600)
       sleep(50)
       stop()
   sleep(20)
  
while True:
  follow_line()

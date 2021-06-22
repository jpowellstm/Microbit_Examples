
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
  

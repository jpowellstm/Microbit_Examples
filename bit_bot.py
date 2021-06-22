
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
  

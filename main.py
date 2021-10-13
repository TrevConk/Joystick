import smbus
import time

class PCF8591:

  def __init__(self,address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))

class Joystick:
  
  def __init__(self,address):
    self.adc = PCF8591(0x48)

  def getX(self):
    self.getX = self.adc.read(0)

  def getY(self):
    self.getY = self.adc.read(1)


joy = Joystick(0x40)

try:
  while(True):
    #print('{:>3},{:>3}'.format(joy.getX, joy.getY))
    print(joy.getX)
    print(joy.getY)
    time.sleep(3)
except Exception as e:
  print(e)
  

  


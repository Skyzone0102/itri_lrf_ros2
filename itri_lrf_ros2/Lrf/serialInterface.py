import serial as Serial

class SerialInterface():
  def __init__(self, port,baudrate = 115200, timeout = 0.5): 
    self.serial=Serial.Serial(port,baudrate,timeout=timeout)

  def open(self,port,baudrate = 115200, timeout = 0.5):
    self.serial=Serial.Serial(port,baudrate,timeout=timeout)

  def write(self,data):
    """
    Write serial data to device
    """
    self.serial.write(bytearray(data,'ascii'))

  def read(self,length):
    """
    Reads and returns amount of length on serial port
    """
    return self.serial.read(length)
    
  def close(self):
    self.serial.close()
    
  def clear(self):
     self.serial.readline()
     self.serial.readline()
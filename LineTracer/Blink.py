import machine
import time

led = machine.Pin('LED', machine.Pin.OUT) #configure LED Pin as an output pin and create and led object for Pin class

while True:
  led.value(True)  #turn on the LED
  time.sleep(1)   #wait for one second
  led.value(False)  #turn off the LED
  time.sleep(1)   #wait for one second

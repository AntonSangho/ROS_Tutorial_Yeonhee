import utime
from machine import Pin

motorA_1 = Pin(16, Pin.OUT)
motorA_2 = Pin(17, Pin.OUT)
motorB_1 = Pin(19, Pin.OUT)
motorB_2 = Pin(18, Pin.OUT)

def forward():
    motorA_1.high()
    motorA_2.low()
    motorB_1.high()
    motorB_2.low()
    
def stop():
    motorA_1.low()
    motorA_2.low()
    motorB_1.low()
    motorB_2.low()
    
def test():
    forward()
    utime.sleep(2)
    stop()
    utime.sleep(2)

for i in range(5):
    test()
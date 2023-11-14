import utime
from machine import Pin, I2C
import ssd1306

# I2C setup
i2c = I2C(0,sda=Pin(4), scl=Pin(5),freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

#Sensor
IR_sens_R = Pin(0, Pin.IN)
IR_sens_M = Pin(1, Pin.IN)
IR_sens_L = Pin(2, Pin.IN)

#Motor 
motorA_1 = Pin(16, Pin.OUT)
motorA_2 = Pin(17, Pin.OUT)
motorB_1 = Pin(19, Pin.OUT)
motorB_2 = Pin(18, Pin.OUT)

def forward():
    motorA_1.high()
    motorA_2.low()
    motorB_1.high()
    motorB_2.low()
    
def left():
    motorA_1.low()
    motorA_2.high()
    motorB_1.high()
    motorB_2.low()

def right():
    motorA_1.high()
    motorA_2.low()
    motorB_1.low()
    motorB_2.high()
    
def stop():
    motorA_1.low()
    motorA_2.low()
    motorB_1.low()
    motorB_2.low()

while True:
    left_detect = int(IR_sens_L.value())
    right_detect = int(IR_sens_R.value())
    middle_detect = int(IR_sens_M.value())
    
    # forward
    if (left_detect == 0 and middle_detect == 1 and right_detect == 0):
        forward()
        display.text('forward', 0, 0, 1)
        display.show()
        utime.sleep(1)
        display.fill(0)
        display.show()
        utime.sleep(1)
        #print("forward")
        #utime.sleep(2)
    elif (left_detect == 1 and middle_detect == 0 and right_detect == 0):
        left()
        display.text('left', 0, 0, 1)
        display.show()
        utime.sleep(1)
        display.fill(0)
        display.show()
        utime.sleep(1)
        #print("left")
        #utime.sleep(2)
    # right
    elif (left_detect == 0 and middle_detect == 0 and right_detect == 1):
        right()
        display.text('right', 0, 0, 1)
        display.show()
        utime.sleep(1)
        display.fill(0)
        display.show()
        utime.sleep(1)
        #print("right")
        #utime.sleep(2)
    # stop
    elif (left_detect == 0 and middle_detect == 0 and right_detect == 0):
        stop()
        display.text('stop', 0, 0, 1)
        display.show()
        utime.sleep(1)
        display.fill(0)
        display.show()
        utime.sleep(1)
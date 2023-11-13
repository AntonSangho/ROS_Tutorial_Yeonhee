from machine import Pin
import time

IR_sens_R = Pin(1, Pin.IN) #오른쪽 센서
IR_sens_M= Pin(2, Pin.IN) #중앙 센서
IR_sens_L = Pin(3, Pin.IN) #왼쪽 센서

while True:
    print(IR_sens_R.value())
    print(IR_sens_M.value())
    print(IR_sens_L.value())
    time.sleep_ms(1000)
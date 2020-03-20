from machine import Pin
import time

def run():
    led1 = Pin('LED1', Pin.OUT_PP)
    while 1:
        led1 = Pin('LED1', Pin.OUT_PP)
        led1.high() # turn on
        time.sleep(2)
        led1.low()  # turn off
        time.sleep(2)

run()
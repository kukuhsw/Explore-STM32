from machine import Pin

led1 = Pin('LED1', Pin.OUT_PP)
led1.high() # turn on
led1.low()  # turn off
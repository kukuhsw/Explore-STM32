from machine import Pin

def run():
    print('demo digital I/O')    
    led = Pin('LED1', Pin.OUT_PP)
    button = Pin('SW', Pin.IN)   
    while 1:
        state = button.value()
        if state == 1:
            led.high()
        else:
            led.low()


# run program
run()


from machine import Pin
import time

gpio_adc = 'A0'
def run():
    print('ADC demo')

    while 1:
        adc = pyb.ADC(Pin(gpio_adc))
        print('ADC: ' + str(adc.read()))
        time.sleep(2)



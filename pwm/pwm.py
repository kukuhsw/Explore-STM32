from machine import Pin
import time

gpio_red = 'D6'
gpio_green = 'D5'
gpio_blue = 'D3'
tim1 = pyb.Timer(1, freq=1000)

def red_color(red):
    pwm_red = Pin(gpio_red)     
    ch_red = tim1.channel(1, pyb.Timer.PWM, pin=pwm_red)
    ch_red.pulse_width_percent(red)

def green_color(green):
    pwm_green = Pin(gpio_green) 
    ch_green = tim1.channel(2, pyb.Timer.PWM, pin=pwm_green)
    ch_green.pulse_width_percent(green)  

def blue_color(blue):
    pwm_blue = Pin(gpio_blue)
    ch_blue = tim1.channel(3, pyb.Timer.PWM, pin=pwm_blue)
    ch_blue.pulse_width_percent(blue)  

def set_rgb(red, green, blue):
    red_color(red)
    green_color(green)
    blue_color(blue)
    time.sleep(2)

def run():
    print('print PWM with RGB led')
    while 1:        
        set_rgb(100, 0, 0) #red        
        set_rgb(0, 100, 0) #green        
        set_rgb(0, 0, 100) #blue        
        set_rgb(100, 100, 0) #yellow        
        set_rgb(30, 0, 30) #purple        
        set_rgb(0, 100, 100) #aqua


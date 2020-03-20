from machine import Pin
import dht
import time

gpio_dht = Pin('D7')
d = dht.DHT22(gpio_dht)

def measure():
    d.measure()
    temperature = d.temperature()    
    humidity = d.humidity()

    return temperature, humidity


def run():
    print('dht module demo')   
    while 1:    
        temp, hum = measure()
        print('Temperature: ' + str(temp) + ' Celsius')
        print('Humidity: ' + str(hum) + ' % RH')        
        time.sleep(2)


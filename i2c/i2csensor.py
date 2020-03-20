from pyb import I2C
import time

# I2C busses
#define MICROPY_HW_I2C1_SCL         (pin_B8)
#define MICROPY_HW_I2C1_SDA         (pin_B9)
#define MICROPY_HW_I2C3_SCL         (pin_H7)
#define MICROPY_HW_I2C3_SDA         (pin_H8)

PCF8591 = 0x48          # I2C bus address
PCF8591_ADC_CH0 = '\x00'  # thermistor
PCF8591_ADC_CH1 = '\x01'  # photo-voltaic cell
PCF8591_ADC_CH3 = '\x03'  # potentiometer

i2c = I2C(1)      
i2c = I2C(1,I2C.MASTER,baudrate=100000)    


# read thermistor
def read_thermistor():    
    i2c.send(PCF8591_ADC_CH0, PCF8591)
    time.sleep(1)
    i2c.recv(1, PCF8591)
    data = i2c.recv(1, PCF8591)
    print('Thermistor: ' + str(ord(chr(data[0]))))

# photo-voltaic cell
def read_photo():    
    i2c.send(PCF8591_ADC_CH1,PCF8591)
    time.sleep(1)
    i2c.recv(1, PCF8591)
    data = i2c.recv(1, PCF8591)
    print('photo-voltaic: ' + str(ord(chr(data[0]))))  

# potentiometer
def read_potentiometer():    
    i2c.send(PCF8591_ADC_CH3, PCF8591)
    time.sleep(1)
    i2c.recv(1, PCF8591)
    data = i2c.recv(1, PCF8591)
    print('potentiometer: ' + str(ord(chr(data[0]))))


def run():
    print('read sensor from i2c protocol')
    while 1:        
        read_thermistor()
        read_photo()
        read_potentiometer()
        time.sleep(2)


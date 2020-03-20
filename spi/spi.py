from pyb import SPI
import random
import time

# D25,PB4 - miso
# D22,PB5 - mosi

def run():
    print('demo spi')    
    spi = SPI(3, SPI.MASTER, baudrate=600000, polarity=1, phase=0, crc=0x7)
    while 1:
        tx = ''.join(chr(random.randint(50,85)) for _ in range(4))
        rx = bytearray(4)

        spi.send_recv(tx,rx)
        
        print('tx: ' + str(tx))
        print('rx: ' + str(rx))

        time.sleep(2)

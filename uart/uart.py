from pyb import UART
import time


# info UART
#define MICROPY_HW_UART2_TX         (pin_D5)
#define MICROPY_HW_UART2_RX         (pin_D6)
#define MICROPY_HW_UART2_RTS        (pin_D4)
#define MICROPY_HW_UART2_CTS        (pin_D3)
#define MICROPY_HW_UART3_TX         (pin_D8)
#define MICROPY_HW_UART3_RX         (pin_D9)
#define MICROPY_HW_UART6_TX         (pin_G14)
#define MICROPY_HW_UART6_RX         (pin_G9)

def run():
    print('demo UART')

    uart = UART(6, 9600)
    uart.init(9600, bits=8, parity=None, stop=1)
    counter = 50
    while 1:
        uart.write(str(counter) + '\r\n')
        print('write uart:' + str(counter))
        time.sleep(2)
        counter += 1
        if counter > 70:
            counter = 50


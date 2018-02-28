# source:
# https://support.microbit.org/support/solutions/articles/19000070728-how-to-read-the-device-serial-number

from microbit import *

display.show('S')

def get_serial_number(format=hex):
    NRF_FICR_BASE = 0x10000000
    DEVICEID_INDEX = 25 # deviceid[1]

    @micropython.asm_thumb
    def reg_read(r0):
        ldr(r0, [r0, 0])
    return format(reg_read(NRF_FICR_BASE + (DEVICEID_INDEX*4)))
    
while True:
    if button_a.was_pressed():
        display.scroll(get_serial_number())
        sleep(1000)
        display.show('S')
        
    sleep(100)

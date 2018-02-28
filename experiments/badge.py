
from microbit import *

people = {
    0x354c70e3:  ('Alice', ['kotlin', 'python']),  # blue 579848
    -0x635cb921: ('Bob', ['kotlin', 'scala']),     # blue 579943
    0x1b0541e0:  ('Carol', ['kotlin']),            # green 532959
    -0x69879749: ('David', ['python']),            # yellow 600778
}

# source:
# https://support.microbit.org/support/solutions/articles/19000070728-how-to-read-the-device-serial-number

def get_device_id():
    NRF_FICR_BASE = 0x10000000
    DEVICEID_INDEX = 25  # deviceid[1]

    @micropython.asm_thumb
    def reg_read(r0):
        ldr(r0, [r0, 0])
    return reg_read(NRF_FICR_BASE + (DEVICEID_INDEX*4))
    
while True:
    name, topics = people[get_device_id()]
    display.scroll(name)
    sleep(1000)

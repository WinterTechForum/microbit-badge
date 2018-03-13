import microbit as mb
import radio

people = {
    0x354c70e3:  ('Alice', ['Kotlin', 'Python']),  # blue 579848
    -0x635cb921: ('Bob',   ['Kotlin', 'Scala']),   # blue 579943
    0x1b0541e0:  ('Carol', ['Kotlin']),            # green 532959
    -0x69879749: ('David', ['Python']),            # yellow 600778
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


radio.on()

name, topics = people[get_device_id()]

while True:
    mb.display.scroll(name.upper() + '  ', delay=120)

    if mb.button_a.was_pressed():
        for topic in topics:
            radio.send(topic)
            mb.display.scroll('#' + topic + ' ', delay=90)

    incoming = radio.receive()
    if incoming in topics:
        mb.display.scroll('#' + incoming + ' ', delay=90)

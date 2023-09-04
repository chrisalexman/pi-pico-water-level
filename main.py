from machine import ADC, Pin
from time import sleep

# pin to get ADC input from water level sensor
water = ADC(Pin(28))

# output pins for LED bar
lvl0 = Pin(15, Pin.OUT)
lvl1 = Pin(14, Pin.OUT)
lvl2 = Pin(13, Pin.OUT)
lvl3 = Pin(12, Pin.OUT)
lvl4 = Pin(11, Pin.OUT)
lvl5 = Pin(6, Pin.OUT)
lvl6 = Pin(7, Pin.OUT)
lvl7 = Pin(8, Pin.OUT)
lvl8 = Pin(9, Pin.OUT)
lvl9 = Pin(5, Pin.OUT)

# range of 15k to 25k in soil
ranges = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

levels = [lvl0, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7, lvl8, lvl9]

# turn off all LEDs before starting
def turn_off_leds():
    for level in levels:
        level.off()

turn_off_leds()

# main loop
while True:

    read_level = water.read_u16()
    level = int(read_level / 1000)

    num_levels = 0

    for index, range in enumerate(ranges):
        if range >= level:
            num_levels = index
            break

    turn_off_leds()

    for lvl in range(num_levels):
        levels[lvl].on()   

    sleep(0.5)

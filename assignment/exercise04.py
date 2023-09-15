"""
Use analog input with photocell
"""

import time
import machine

led = machine.Pin("LED", machine.Pin.OUT)
adc = machine.ADC(28)

blink_period = 0.1

max_bright = 13000
min_bright = 9000

while True:
    value = adc.read_u16()
    print(value)
    # %% need to clip duty cycle to range [0, 1]

    duty_cycle = (value - min_bright) / (max_bright - min_bright)
    # this equation will give values outside the range [0, 1]

    # %% clip duty cycle to range [0, 1]
    if duty_cycle < 0:
        duty_cycle = 0
    elif duty_cycle > 1:
        duty_cycle = 1

    led.high()
    time.sleep(blink_period * duty_cycle)
    led.low()
    time.sleep(blink_period * (1 - duty_cycle))

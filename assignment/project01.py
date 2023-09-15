"""
Response time - single-threaded
"""

from machine import Pin
import time
import random


led = Pin("LED", Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_UP)

N: int = 5
sample_ms = 10.0
on_ms = 500


def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


t: list[float | None] = []

blinker(3)

for i in range(N):
    time.sleep(random_time_interval(0.5, 5.0))

    led.high()

    tic = time.ticks_ms()
    t0 = None
    while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
        if button.value() == 0:
            t0 = time.ticks_diff(time.ticks_ms(), tic)
            led.low()
            break
    t.append(t0)

    led.low()

blinker(5)

# %% collate results
misses = t.count(None)
print(f"You missed the light {misses} / {N} times")

t_good = [x for x in t if x is not None]

# how to print the average, min, max response time?

print(t_good)
sum_average = sum(t_good)
length = len(t_good)
avg = sum_average / length
print(f"This is the average: {avg}\n")
max_value = max(t_good)
print(f"This is the max: {max_value}\n")
min_value = min(t_good)
print(f"This is the min: {min_value}\n")

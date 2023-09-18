import machine
import time
import _thread
import json
import random

# Setup
led = machine.Pin("LED", machine.Pin.OUT)
button1 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
adc = machine.ADC(2)
N = 1
sample_interval_s = 0.5
t1_global = []
t2_global = []

def random_time_interval(tmin: float, tmax: float) -> float:
    """Return a random time interval between min and max."""
    return random.uniform(tmin, tmax)

def light_logger(N: int, sample_interval_s: float) -> None:
    values = []
    for _ in range(N):
        values.append(adc.read_u16())
        time.sleep(sample_interval_s)
    print(values)
    
def reaction_game(N: int, t1_global, t2_global):
    t1 = []
    t2 = []
    for _ in range(N):
        time.sleep(random_time_interval(0.5, 5.0))
        led.high()

        tic = time.ticks_ms()
        while True:
            if not button1.value():
                t1.append(time.ticks_diff(time.ticks_ms(), tic))
                break
            elif not button2.value():
                t2.append(time.ticks_diff(time.ticks_ms(), tic))
                break

        led.low()
        
    t1_global = t1
    t2_global = t2
    return t1_global, t2_global

_thread.start_new_thread(light_logger, (N, sample_interval_s))
reaction_game(N, t1_global, t2_global)

print(t1_global)
sum_average_t1 = sum(t1_global)
length_t1 = len(t1_global)
avg_t1 = sum_average_t1 / length_t1
print(f"This is the average for P1: {avg_t1}\n")
max_value_t1 = max(t1_global)
print(f"This is the max for P1: {max_value_t1}\n")
min_value_t1 = min(t1_global)
print(f"This is the min for P1: {min_value_t1}\n")

print(t2_global)
sum_average_t2 = sum(t2_global)
length_t2 = len(t2_global)
avg_t2 = sum_average_t2 / length_t2
print(f"This is the average for P2: {avg_t2}\n")
max_value_t2 = max(t2_global)
print(f"This is the max for P2: {max_value_t2}\n")
min_value_t2 = min(t2_global)
print(f"This is the min for P2: {min_value_t2}\n")


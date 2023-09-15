import machine
import time
import _thread
import json
import random

# Setup
led = machine.Pin("LED", machine.Pin.OUT)
button1 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
adc = machine.ADC(28)
N = 10

def random_time_interval(tmin: float, tmax: float) -> float:
    """Return a random time interval between min and max."""
    return random.uniform(tmin, tmax)

def light_logger(N: int, sample_interval_s: float) -> None:
    values = []
    for _ in range(N):
        values.append(adc.read_u16())
        time.sleep(sample_interval_s)
    
    with open('light_data.json', 'w') as f:
        json.dump({"light_values": values}, f)

def reaction_game(N: int):
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

    with open('reaction_data.json', 'w') as f:
        data = {
            "player1_times": t1,
            "player2_times": t2,
            "min_time_player1": min(t1) if t1 else None,
            "min_time_player2": min(t2) if t2 else None,
            "max_time_player1": max(t1) if t1 else None,
            "max_time_player2": max(t2) if t2 else None,
            "avg_time_player1": sum(t1)/len(t1) if t1 else None,
            "avg_time_player2": sum(t2)/len(t2) if t2 else None,
            "misses_player1": N - len(t1),
            "misses_player2": N - len(t2)
        }
        json.dump(data, f)

# Read parameters from JSON file
with open('parameters.json', 'r') as f:
    params = json.load(f)
    N = params.get("N", 10)
    sample_interval_s = params.get("sample_interval_s", 0.5)

_thread.start_new_thread(light_logger, (N, sample_interval_s))
reaction_game(N)

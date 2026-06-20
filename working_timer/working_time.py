import time

def working(minutes):
    seconds = minutes * 60
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
    return seconds
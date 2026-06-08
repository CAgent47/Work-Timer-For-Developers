import time

def working(minutes):
    """
    Countdown timer function based on minutes
    Args:
        minutes: Number of minutes for countdown
    Returns:
        seconds_remaining: Remaining seconds after countdown
    """
    seconds = minutes * 60
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
    return seconds

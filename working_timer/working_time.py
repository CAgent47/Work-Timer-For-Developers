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
        print(f"Time remaining: {seconds // 60:02d}:{seconds % 60:02d}")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
    return seconds
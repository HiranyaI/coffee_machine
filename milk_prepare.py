import utils

def milk_preperation(drink_type, times):
    seconds = times.get(drink_type, 0)
    if seconds > 0:
        utils.countdown(seconds, f"{drink_type} Milk")
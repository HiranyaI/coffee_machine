import time

def countdown(seconds, task_label):
    """A shared timer that updates on a single line."""
    t = seconds
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"[{task_label}] {timer} remaining...", end='\r')  
        time.sleep(1)
        t -= 1
    print(f"{task_label} completed!           ")
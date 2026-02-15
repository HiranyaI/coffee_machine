import time

def shots(number_of_shots):
    if number_of_shots==int(2):
        t=20
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')  
            time.sleep(1)
            t -= 1
        print(f"{number_of_shots} extracted from machine.")

    elif number_of_shots==int(3):
        t=30
        while t:
            mins,secs = divmod(t,60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')  
            time.sleep(1)
            t -= 1
        print(f"{number_of_shots} extracted from the machine.")


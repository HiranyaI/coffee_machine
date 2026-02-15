import time

def milk_preperation(drink_type):
    if drink_type == "flatwhite":
        t=45
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')  
            time.sleep(1)
            t -= 1
        print(f"Milk for {drink_type} is finished.")
    
    elif drink_type == "latte":
        t=20
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')  
            time.sleep(1)
            t -= 1
        print(f"Milk for {drink_type} is finished.")

    elif drink_type == "cappucino":
        t=25
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')  
            time.sleep(1)
            t -= 1
        print(f"Milk for {drink_type} is finished.")

    elif drink_type == "cortado":
        t=15
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')  
            time.sleep(1)
            t -= 1
        print(f"Milk for {drink_type} is finished.")
    
    elif drink_type == "hotchocolate":
        t=40
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')  
            time.sleep(1)
            t -= 1
        print(f"Milk for {drink_type} is finished.")
    
    elif drink_type == "mocha":
        t=25
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')  
            time.sleep(1)
            t -= 1
        print(f"Milk for {drink_type} is finished.")
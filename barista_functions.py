#This is the file for barista
import time
import milk_prepare
import shots_prepare
import random

drinks=["latte","cappucino","flatwhite","mocha","hotchocolate"]
group_heads_in_use=0

def make_drink(drink_type):
    if drink_type == "latte":
        milk_prepare.milk_preperation(drink_type)
        shots_prepare.shots(2)
    elif drink_type== "cappucino":
        milk_prepare.milk_preperation(drink_type)
        shots_prepare.shots(3)
    elif drink_type== "cortado":
        milk_prepare.milk_preperation(drink_type)
        shots_prepare.shots(2)
    elif drink_type== "flatwhite":
        milk_prepare.milk_preperation(drink_type)
        shots_prepare.shots(3)
    elif drink_type== "mocha":
        milk_prepare.milk_preperation(drink_type)
        shots_prepare.shots(3)
    elif drink_type=="hotchocolate":
        milk_prepare.milk_preperation(drink_type)
    else:
        print("Sorry we don't have that drink. Thank You!")
        
    t=5
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  
        time.sleep(1)
        t -= 1
    print(f"{drink_type} served to the customer")
    group_heads_in_use=group_heads_in_use-1

make_drink("latte")

if group_heads_in_use==3:
    print("Please wait till one group handle is free.")


random_drink=drinks[random.randrange(0,4)]
print(random_drink)

for i in range(0,10):
    print(i)
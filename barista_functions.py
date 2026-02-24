import threading
import random
import time
import utils

# group handles = 3 orders per time
machine_capacity = threading.Semaphore(3)

#Menu of drinks
MENU = {
    "latte": {"milk": 20, "shots": 20, "num_shots": 2},
    "flatwhite": {"milk": 45, "shots": 30, "num_shots": 3},
    "cappucino": {"milk": 25, "shots": 30, "num_shots": 3},
    "mocha": {"milk": 25, "shots": 30, "num_shots": 3},
    "cortado": {"milk": 15, "shots": 20, "num_shots": 2},
    "hotchocolate": {"milk": 40, "shots": 0, "num_shots": 0}
}

def make_drink(order_id, drink_type):
    """Handles the full lifecycle of one drink."""
    with machine_capacity:
        print(f"\n[BARISTA] Starting Order #{order_id}: {drink_type}")
        
        #Getting ready time
        prep_time = random.randint(5, 10)
        utils.countdown(prep_time, f"Order #{order_id} starting to prepare")

        recipe = MENU[drink_type]

        #Milk prepare
        if recipe["milk"] > 0:
            utils.countdown(recipe["milk"], f"Order #{order_id} Milk")
        
        #Shots preparing
        if recipe["shots"] > 0:
            utils.countdown(recipe["shots"], f"Order #{order_id} Shots")

        print(f"\nOrder #{order_id} ({drink_type}) is served to the customer!")

def start_coffee_shop():
    """Main loop that randomly generates orders."""
    print("---Coffee Machine is On, Accepting orders---")
    order_counter = 1
    
    try:
        while True:
            #Pick a random drink and pass it to barista
            drink_choice = random.choice(list(MENU.keys()))
            
            #Order in a new thread
            t = threading.Thread(target=make_drink, args=(order_counter, drink_choice))
            t.daemon = True #When user stop it System stops
            t.start()
            
            order_counter += 1
            
            #Random time to next customer
            wait_for_customer = random.randint(3, 15)
            time.sleep(wait_for_customer)
            
    except KeyboardInterrupt:
        print("\n--- Coffee Machine is Closing. Cleaning the machine! ---")

if __name__ == "__main__":
    start_coffee_shop()
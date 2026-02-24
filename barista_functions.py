import threading
import random
import time
import utils

# Requirements from README: 3 orders max at a time
machine_capacity = threading.Semaphore(3)

# Drinks and their specific timings from your original files
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
        
        # Requirement from README: Barista prep time (5-10s)
        prep_time = random.randint(5, 10)
        utils.countdown(prep_time, f"Order #{order_id} Prep")

        recipe = MENU[drink_type]

        # Process Milk
        if recipe["milk"] > 0:
            utils.countdown(recipe["milk"], f"Order #{order_id} Milk")
        
        # Process Shots
        if recipe["shots"] > 0:
            utils.countdown(recipe["shots"], f"Order #{order_id} Shots")

        print(f"\n☕ Order #{order_id} ({drink_type}) is served to the customer!")

def start_coffee_shop():
    """Main loop that randomly generates orders."""
    print("---Coffee Machine is On, Accepting orders---")
    order_counter = 1
    
    try:
        while True:
            # Randomly pick a drink from your list
            drink_choice = random.choice(list(MENU.keys()))
            
            # Start the order in a new thread
            t = threading.Thread(target=make_drink, args=(order_counter, drink_choice))
            t.daemon = True # Allows the program to close when you stop it
            t.start()
            
            order_counter += 1
            
            # Wait a random amount of time before the next customer arrives (3-15 seconds)
            wait_for_customer = random.randint(3, 15)
            time.sleep(wait_for_customer)
            
    except KeyboardInterrupt:
        print("\n--- Shop is closing. Cleaning the machine! ---")

if __name__ == "__main__":
    start_coffee_shop()
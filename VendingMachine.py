## The Brief
# Your task is to create a Vending Machine program using the Python programming language.
# The program should demonstrate your knowledge of programming and make use of the techniques introduced over the course of the module.
# Your application should be accompanied by a development document (1,000 - 1,500 words).

## The Application
# The Vending Machine must have the following features as a minimum requirement:
# - A menu of drinks and snacks presented via the console. The number and range is up to you.
# - A set of numbers or codes that the user can input to select a particular drink or snack.
# - A way of managing money so the user can input any amount of money and have the correct change returned.
# - A message that tells the user that a particular drink or snack has been dispensed.
# - A message that tells the user how much change they have received.
# - Comments in the code to explain key operations.

# You may wish to add additional features to your Vending Machine to achieve higher marks.
# Below is an indication of some of these features, however you may also wish to come up with your own:
# - A method of categorising items in the vending machine to improve the user experience (e.g. 'Chocolate' or 'Hot Drinks').
# - A way of allowing users to buy additional items.
# - Appropriate error checking to validate inputs and ensure the user has enough money.
# - An intelligence system for suggesting purchase. For examples, if you buy a coffee, the vending machine may suggest that you buy biscuits.
# - A stock system meaning the machine may run out of products.

# To achieve marks in the higher mark boundaries you should be aiming to implement the more advanced techniques covered in the module including use of functions and object oriented programming.

## Input:

def display_menu(items):
    # Display the vending machine menu with item codes, names, prices, and stock levels.
    print("\n--- Welcome to Ai's Vending Machine! ---\n")
    print("Code | Item             | Price  | Stock")
    print("-----------------------------------------")
    for code, item in items.items():
        print(f"{code:<4} | {item['name']:<15} | AED {item['price']:<5} | {item['stock']}")

def insert_money(balance):
    # Allow the user to insert money and add it to their balance.
    while True:
        try:
            print(f"\nYour current balance is: AED {balance:.2f}")
            amount = float(input("Add money (e.g., 0.50, 1.00) or 0 to continue: AED "))
            if amount >= 0:
                return balance + amount
            else:
                print("Please enter a positive amount.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def suggest_item(items, current_item):
    # Suggest an additional item to the user based on their current purchase.
    suggestions = {
        "Coffee": "Biscuits",
        "Tea": "Cookies",
        "Water Bottle": "Chips",
        "Soda Can": "Chocolate Bar",
        "Green Tea": "Biscuits",
        "Energy Drink": "Chips",
    }
    suggestion = suggestions.get(current_item['name'])
    if suggestion:
        for code, item in items.items():
            if item['name'] == suggestion and item['stock'] > 0:
                print(f"\nSuggested item: {item['name']} (AED {item['price']:.2f})")
                break

def select_item(items, balance):
    # Allow the user to select an item and check if they have enough balance to purchase it.
    while True:
        code = input("\nEnter the code of the item you want to purchase: ").upper()
        if code in items:
            item = items[code]
            if item['stock'] > 0:
                if balance >= item['price']:
                    balance -= item['price']
                    item['stock'] -= 1
                    print(f"\nDispensing {item['name']} from {item['category']}... Enjoy!")
                    print(f"Remaining balance: AED {balance:.2f}")
                    suggest_item(items, item)
                    return balance
                else:
                    print(f"\nYou need AED {item['price'] - balance:.2f} more to buy {item['name']}.")
                    return balance
            else:
                print(f"\nSorry, {item['name']} is out of stock.")
                return balance
        else:
            print("Invalid code. Please try again.")

def vending_machine():
    # Main vending machine function to initialize items, handle user interaction, and manage balance.
    items = {
        "A1": {"name": "Chocolate Bar", "price": 1.50, "stock": 10, "category": "Snacks"},
        "A2": {"name": "Chips", "price": 1.00, "stock": 15, "category": "Snacks"},
        "B1": {"name": "Water Bottle", "price": 0.80, "stock": 20, "category": "Drinks"},
        "B2": {"name": "Soda Can", "price": 1.20, "stock": 12, "category": "Drinks"},
        "C1": {"name": "Coffee", "price": 1.50, "stock": 8, "category": "Hot Drinks"},
        "C2": {"name": "Tea", "price": 1.30, "stock": 10, "category": "Hot Drinks"},
        "C3": {"name": "Green Tea", "price": 1.70, "stock": 6, "category": "Hot Drinks"},
        "D1": {"name": "Biscuits", "price": 2.00, "stock": 5, "category": "Snacks"},
        "D2": {"name": "Cookies", "price": 1.80, "stock": 7, "category": "Snacks"},
        "E1": {"name": "Energy Drink", "price": 2.50, "stock": 10, "category": "Drinks"},
        "E2": {"name": "Fruit Juice", "price": 2.20, "stock": 12, "category": "Drinks"},
        "F1": {"name": "Protein Bar", "price": 3.00, "stock": 8, "category": "Health Snacks"},
        "F2": {"name": "Granola Bar", "price": 2.80, "stock": 10, "category": "Health Snacks"},
    }
    balance = 0.0

    print("\nHello! Let's make your vending experience special!")
    while True:
        display_menu(items)  # Display the vending machine menu.
        balance = insert_money(balance)  # Allow the user to add money to their balance.
        balance = select_item(items, balance)  # Let the user select an item to purchase.
        more = input("\nDo you want to buy another item? (yes/no): ").lower()
        if more != "yes":
            print(f"\nReturning your change: AED {balance:.2f}")
            print("\nThank you for choosing Ai's Vending Machine. See you next time!")
            break

if __name__ == "__main__":
    vending_machine()

## Output:

# Hello! Let's make your vending experience special!
# 
# --- Welcome to Ai's Vending Machine! --- 
# 
# Code | Item             | Price  | Stock 
# -----------------------------------------
# A1   | Chocolate Bar   | AED 1.5   | 10  
# A2   | Chips           | AED 1.0   | 15
# B1   | Water Bottle    | AED 0.8   | 20
# B2   | Soda Can        | AED 1.2   | 12
# C1   | Coffee          | AED 1.5   | 8
# C2   | Tea             | AED 1.3   | 10
# C3   | Green Tea       | AED 1.7   | 6
# D1   | Biscuits        | AED 2.0   | 5
# D2   | Cookies         | AED 1.8   | 7
# E1   | Energy Drink    | AED 2.5   | 10
# E2   | Fruit Juice     | AED 2.2   | 12
# F1   | Protein Bar     | AED 3.0   | 8
# F2   | Granola Bar     | AED 2.8   | 103
# 
# Your current balance is: AED 0.00
# Add money (e.g., 0.50, 1.00) or 0 to continue: AED 30
# 
# Enter the code of the item you want to purchase: A1
# 
# Dispensing Chocolate Bar from Snacks... Enjoy!
# Remaining balance: AED 28.50
# 
# Do you want to buy another item? (yes/no): yes
# 
# --- Welcome to Ai's Vending Machine! ---
# 
# Code | Item             | Price  | Stock
# -----------------------------------------
# A1   | Chocolate Bar   | AED 1.5   | 9
# A2   | Chips           | AED 1.0   | 15
# B1   | Water Bottle    | AED 0.8   | 20
# B2   | Soda Can        | AED 1.2   | 12
# C1   | Coffee          | AED 1.5   | 8
# C2   | Tea             | AED 1.3   | 10
# C3   | Green Tea       | AED 1.7   | 6
# D1   | Biscuits        | AED 2.0   | 5
# D2   | Cookies         | AED 1.8   | 7
# E1   | Energy Drink    | AED 2.5   | 10
# E2   | Fruit Juice     | AED 2.2   | 12
# F1   | Protein Bar     | AED 3.0   | 8
# F2   | Granola Bar     | AED 2.8   | 10
# 
# Your current balance is: AED 28.50
# Add money (e.g., 0.50, 1.00) or 0 to continue: AED 5
# 
# Enter the code of the item you want to purchase: a2
# 
# Dispensing Chips from Snacks... Enjoy!
# Remaining balance: AED 32.50
# 
# Do you want to buy another item? (yes/no): yes
# 
# --- Welcome to Ai's Vending Machine! ---
# 
# Code | Item             | Price  | Stock
# -----------------------------------------
# A1   | Chocolate Bar   | AED 1.5   | 9
# A2   | Chips           | AED 1.0   | 14
# B1   | Water Bottle    | AED 0.8   | 20
# B2   | Soda Can        | AED 1.2   | 12
# C1   | Coffee          | AED 1.5   | 8
# C2   | Tea             | AED 1.3   | 10
# C3   | Green Tea       | AED 1.7   | 6
# D1   | Biscuits        | AED 2.0   | 5
# D2   | Cookies         | AED 1.8   | 7
# E1   | Energy Drink    | AED 2.5   | 10
# E2   | Fruit Juice     | AED 2.2   | 12
# F1   | Protein Bar     | AED 3.0   | 8
# F2   | Granola Bar     | AED 2.8   | 10
# 
# Your current balance is: AED 32.50
# Add money (e.g., 0.50, 1.00) or 0 to continue: AED b1
# Invalid input. Please enter a valid amount.
# 
# Your current balance is: AED 32.50
# Add money (e.g., 0.50, 1.00) or 0 to continue: AED 0
# 
# Enter the code of the item you want to purchase: b1
# 
# Dispensing Water Bottle from Drinks... Enjoy!
# Remaining balance: AED 31.70
# 
# Suggested item: Chips (AED 1.00)
# 
# Do you want to buy another item? (yes/no): no
# 
# Returning your change: AED 31.70
# 
# Thank you for choosing Ai's Vending Machine. See you next time!
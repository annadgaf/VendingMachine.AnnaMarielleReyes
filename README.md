## The Brief
# Youser task is to create a Vending Machine program using the Python programming language.
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
    print("\nWelcome to Ai's Vending Machine!\n")
    print("Code | Item          | Price  | Stock")
    print("---------------------------------")
    for code, item in items.items():
        print(f"{code:<4} | {item['name']:<12} | ${item['price']:<5} | {item['stock']}")

def insert_money(balance):
    while True:
        try:
            print(f"\nCurrent balance: ${balance:.2f}")
            amount = float(input("Enter additional money (e.g., 0.50, 1.00) or 0 to skip: $"))
            if amount >= 0:
                return balance + amount
            else:
                print("Please insert a positive amount.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def select_item(items, balance):
    while True:
        code = input("\nEnter the code of the item you want to purchase: ").upper()
        if code in items:
            item = items[code]
            if item['stock'] > 0:
                if balance >= item['price']:
                    balance -= item['price']
                    item['stock'] -= 1
                    print(f"Dispensing {item['name']}... Enjoy and have a nice day!")
                    print(f"Remaining balance: ${balance:.2f}")
                else:
                    print(f"Insufficient balance. {item['name']} costs ${item['price']:.2f}.")
                    return balance
            else:
                print(f"Sorry, {item['name']} is out of stock.")
                return balance
        else:
            print("Invalid code. Please try again.")

def vending_machine():
    items = {
        "A1": {"name": "Chocolate Bar", "price": 1.50, "stock": 10},
        "A2": {"name": "Chips", "price": 1.00, "stock": 15},
        "B1": {"name": "Bottled Water", "price": 0.80, "stock": 20},
        "B2": {"name": "Soda Can", "price": 1.20, "stock": 12},
        "C1": {"name": "Coffee", "price": 1.50, "stock": 8},
        "C2": {"name": "Tea", "price": 1.30, "stock": 10},
    }
    balance = 0.0

    while True:
        display_menu(items)
        balance = insert_money(balance)
        balance = select_item(items, balance)
        more = input("\nWould you like to buy another item? (yes/no): ").lower()
        if more != "yes":
            print(f"Returning change: ${balance:.2f}")
            print("\nThank you for using Ai's Vending Machine!")

if __name__ == "__main__":
    vending_machine()

## Output:

# Welcome to Ai's Vending Machine!
#
# Code | Item          | Price  | Stock
# ---------------------------------    
# A1   | Chocolate Bar | $1.5   | 10   
# A2   | Chips        | $1.0   | 15    
# B1   | Bottled Water | $0.8   | 20
# B2   | Soda Can     | $1.2   | 12
# C1   | Coffee       | $1.5   | 8
# C2   | Tea          | $1.3   | 10
#
# Current balance: $0.00
# Enter additional money (e.g., 0.50, 1.00) or 0 to skip: $10
#
# Enter the code of the item you want to purchase: A1
# Dispensing Chocolate Bar... Enjoy and have a nice day!
# Remaining balance: $8.50
#
# Enter the code of the item you want to purchase: a2
# Dispensing Chips... Enjoy and have a nice day!
# Remaining balance: $7.50
# 
# Enter the code of the item you want to purchase: a1
# Dispensing Chocolate Bar... Enjoy and have a nice day!
# Remaining balance: $6.00
#
# Enter the code of the item you want to purchase: b1
# Dispensing Bottled Water... Enjoy and have a nice day!
# Remaining balance: $5.20
#
# Enter the code of the item you want to purchase: B2
# Dispensing Soda Can... Enjoy and have a nice day!
# Remaining balance: $4.00
#
# Enter the code of the item you want to purchase: c1
# Dispensing Coffee... Enjoy and have a nice day!
# Remaining balance: $2.50
#
# Enter the code of the item you want to purchase: C1
# Dispensing Coffee... Enjoy and have a nice day!
# Remaining balance: $1.00
#
# Enter the code of the item you want to purchase: a1
# Insufficient balance. Chocolate Bar costs $1.50.
#
# Would you like to buy another item? (yes/no): yes
#
# Welcome to Ai's Vending Machine!
#
# Code | Item          | Price  | Stock
# ---------------------------------
# A1   | Chocolate Bar | $1.5   | 8
# A2   | Chips        | $1.0   | 14
# B1   | Bottled Water | $0.8   | 19
# B2   | Soda Can     | $1.2   | 11
# C1   | Coffee       | $1.5   | 6
# C2   | Tea          | $1.3   | 10
#
# Current balance: $1.00
# Enter additional money (e.g., 0.50, 1.00) or 0 to skip: $0 
# 
# Enter the code of the item you want to purchase: a2
# Dispensing Chips... Enjoy and have a nice day!
# Remaining balance: $0.00
#
# Enter the code of the item you want to purchase: c2
# Insufficient balance. Tea costs $1.30.
#
# Would you like to buy another item? (yes/no): yes
# 
# Welcome to Ai's Vending Machine!
#
# Code | Item          | Price  | Stock
# ---------------------------------
# A1   | Chocolate Bar | $1.5   | 8
# A2   | Chips        | $1.0   | 13
# B1   | Bottled Water | $0.8   | 19
# B2   | Soda Can     | $1.2   | 11
# C1   | Coffee       | $1.5   | 6
# C2   | Tea          | $1.3   | 10
#
# Current balance: $0.00
# Enter additional money (e.g., 0.50, 1.00) or 0 to skip: $-2
# Please insert a positive amount.
#
# Current balance: $0.00
# Enter additional money (e.g., 0.50, 1.00) or 0 to skip: $0
#
# Enter the code of the item you want to purchase: a1
# Insufficient balance. Chocolate Bar costs $1.50.
#
# Would you like to buy another item? (yes/no): no
# Returning change: $0.00
#
# Thank you for using Ai's Vending Machine!
#
# Welcome to Ai's Vending Machine!
#
# Code | Item          | Price  | Stock
# ---------------------------------
# A1   | Chocolate Bar | $1.5   | 8
# A2   | Chips        | $1.0   | 13
# B1   | Bottled Water | $0.8   | 19
# B2   | Soda Can     | $1.2   | 11
# C1   | Coffee       | $1.5   | 6
# C2   | Tea          | $1.3   | 10
#
# Current balance: $0.00
# Enter additional money (e.g., 0.50, 1.00) or 0 to skip: $

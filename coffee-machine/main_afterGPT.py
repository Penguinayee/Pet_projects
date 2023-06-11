MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#3 Print report
def print_report():
    print("Water:", resources["water"], "ml")
    print("Milk:", resources["milk"], "ml")
    print("Coffee:", resources["coffee"], "g")
    print("Money: $", profit)


#4 Check resources sufficient
def check_resource(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True


#5 Process coins
def process_coins():
    q = int(input("How many querters?") or "0")
    d = int(input("How many dimes?") or "0")
    n = int(input("How many nickles?") or "0")
    p = int(input("How many pennies?") or "0")
    return q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01


#6 Check transaction successful?
def check_transaction(order_drink, insert):
    if MENU[order_drink]["cost"] > insert:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


#7. Make Coffee.
def make_coffee(order_drink, insert):
    #insert = process_coins(q, d, n, p)
    if not check_resource(order_drink):
        return
    if not check_transaction(order_drink, insert):
        return
    
    resources["water"] = resources["water"] - MENU[order_drink]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[order_drink]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[order_drink]["ingredients"]["coffee"]
    
    global profit
    profit += MENU[order_drink]["cost"]
    change = insert - MENU[order_drink]["cost"]

    print(f"Here is ${change:.2f} dollars in change.")
    print(f"Here is your {order_drink}. Enjoy!")

    
#1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
order = input("What would you like? (espresso/latte/cappuccino):")

while True:
#2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if order == "off":
        break
    elif order == "report":
        print_report()
    elif order not in ["espresso", "latte", "cappuccino"]:
        print("Sorry. I don't understand.")
    else:
        insert = process_coins()
        make_coffee(order, insert)

    order = input("What would you like? (espresso/latte/cappuccino):")


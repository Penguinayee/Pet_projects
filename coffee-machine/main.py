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
def check_resource(drink, resources = resources):
    if resources["water"] <= MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        drink = None
    elif resources["milk"] <= MENU[drink]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        drink = None
    elif resources["coffee"] <= MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        drink = None
    else:
        drink = drink
    return drink


#5 Process coins
def process_coins(q, d, n, p):
    return int(q*0.25 + d*0.1 + n*0.05 + p*0.01)


#6 Check transaction successful?
def check_transaction(order_drink, insert, res = resources):
    if MENU[order_drink]["cost"] > insert:
        return print("Sorry that's not enough money. Money refunded.")
    if MENU[order_drink]["cost"] <= insert:
        order_drink = check_resource(order_drink, res)
        if order_drink == None:
            return
        earned = MENU[order_drink]["cost"]
        change = insert - MENU[order_drink]["cost"]
        print(f"Here is ${change} dollars in change.")
    return order_drink, earned


#7. Make Coffee.
def make_coffee(order_drink, q, d, n, p, res = resources, prof = profit):
    insert = process_coins(q, d, n, p)
    order_drink, earned= check_transaction(order_drink, insert, res)    
    res["water"] = res["water"] - MENU[order_drink]["ingredients"]["water"]
    res["milk"] = res["milk"] - MENU[order_drink]["ingredients"]["milk"]
    res["coffee"] = res["coffee"] - MENU[order_drink]["ingredients"]["coffee"]
    prof = prof + earned
    print(f"Here is your {order_drink}. Enjoy!")
    return res, prof

    
#1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
order = input("What would you like? (espresso/latte/cappuccino):")

while order not in ["espresso", "latte", "cappuccino", "report", "off"]:
    print("Sorry. I don't understand.")
    order = input("What would you like? (espresso/latte/cappuccino):")

#2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if order == "off":
        break
    elif order == "report":
        print_report
        order = input("What would you like? (espresso/latte/cappuccino):")
    else:
        print(f"{order} is MENU[{order}]["cost"])
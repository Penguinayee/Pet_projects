from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while True:
    #1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
    order_name = input(f"What would you like? ({menu.get_items()}):")
    drink = menu.find_drink(order_name)
    #2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if order_name == "off":
        break
    #3. Print report.
    elif order_name == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        #4. Check resources sufficient?
        if coffee_maker.is_resource_sufficient(drink):
            #5. Process coins
            #6. Check transaction successful?
            if money_machine.make_payment(drink.cost):
                #7. Make Coffee.
                coffee_maker.make_coffee(drink)



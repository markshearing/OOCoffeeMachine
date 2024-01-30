from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True

theMenu = Menu()
theMachine = CoffeeMaker()
theMoney = MoneyMachine()

while is_on:
    drinkChoice = input(f"What would you like? ({theMenu.get_items()}): ")
    if drinkChoice == "off":
        is_on = False
    elif drinkChoice == "report":
        theMachine.report()
        theMoney.report()
    else:
        # Get a Menu Item object based on the drink choice
        menuItem = theMenu.find_drink(drinkChoice)
        if menuItem is not None and theMachine.is_resource_sufficient(menuItem):
            # Ask for the money for the drink based on the menuItem cost
            if theMoney.make_payment(menuItem.cost):
                theMachine.make_coffee(menuItem)

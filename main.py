from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What type of coffee would you like?({options})\n").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        # Reports
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
            # Resources Sufficient
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)







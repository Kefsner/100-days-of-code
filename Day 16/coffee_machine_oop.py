from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time
import menu

is_on = True

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

while is_on:
    order = input(f"What would you like? {my_menu.get_items()}\n")
    if order == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif order == "off":
        is_on = False
        print("Goodbye!")
        time.sleep(3)
    else:
        MenuItem.name = order
        MenuItem.cost = menu.MENU[order]["cost"]
        MenuItem.ingredients = menu.MENU[order]["ingredients"]

        if my_coffee_maker.is_resource_sufficient(MenuItem):
            my_coffee_maker.make_coffee(MenuItem)
            my_money_machine.make_payment(MenuItem.cost)

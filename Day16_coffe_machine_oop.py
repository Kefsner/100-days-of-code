from Day16_coffe_machine_oop_menu import Menu, MenuItem
from Day16_coffe_machine_oop_coffee_maker import CoffeeMaker
from Day16_coffe_machine_oop_money_machine import MoneyMachine
import time
import Day15_coffe_machine_data

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
        MenuItem.cost = Day15_coffe_machine_data.MENU[order]["cost"]
        MenuItem.ingredients = Day15_coffe_machine_data.MENU[order]["ingredients"]

        if my_coffee_maker.is_resource_sufficient(MenuItem):
            my_coffee_maker.make_coffee(MenuItem)
            my_money_machine.make_payment(MenuItem.cost)

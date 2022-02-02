from Day15_coffe_machine_data import MENU
from Day15_coffe_machine_data import resources
import time

turn_off = False

profit = 0


def check_admin(check):
    if check == "report" or check == "off":
        password = input("Password: ")
        if password == "admin123":
            return True
        else:
            return False


def check_user(check):
    if check == "espresso" or check == "latte" or check == "cappuccino":
        return True


def check_resources(check):
    for ingredients in check:
        if resources[ingredients] >= check[ingredients]:
            continue
        else:
            print(f"There is not enough {ingredients}")
            return False
    return True


while not turn_off:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    admin = check_admin(order)
    if admin:
        if order == "off":
            turn_off = True
            print("Goodbye!")
            time.sleep(3)
        if order == "report":
            for key in resources:
                print(f'{key}: {resources[key]}')
            print(f'Money: ${profit}')
    elif order == "off" or order == "report":
        print("Invalid password.")

    elif check_user(order):
        if check_resources(MENU[order]["ingredients"]):
            print(f'A {order} costs ${MENU[order]["cost"]}. Please insert coins.')
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            payment = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
            if payment >= MENU[order]["cost"]:
                change = round(payment - MENU[order]["cost"], 2)
                profit += payment - change
                print(f"Here is ${change} in change.")
                print("Enjoy your coffee!")
                for each in resources:
                    resources[each] = resources[each] - MENU[order]["ingredients"][each]
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Please type a valid input.")

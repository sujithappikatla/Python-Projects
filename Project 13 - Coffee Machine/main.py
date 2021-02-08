from art import logo

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_profit = 0


def print_report():
    """Print Report of Remaining resources and profit"""
    print(f"Water : {resources['water']}")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")
    print(f"Money : {total_profit}")


def valid_menu_item(user_input):
    """Check if user inputted entry is in MENU"""
    if user_input in MENU:
        return True
    return False


def resources_available(user_input):
    """check if resources are available for making drink"""
    for resource in MENU[user_input]['ingredients']:
        if MENU[user_input]['ingredients'][resource] > resources[resource]:
            print(f"Sorry there is not enough {resource}")
            return False
    return True


def update_resources(user_input):
    """Update resources after making drink"""
    global total_profit
    global resources
    total_profit += MENU[user_input]['cost']
    for resource in MENU[user_input]['ingredients']:
        resources[resource] -= MENU[user_input]['ingredients'][resource]


def bill_check(user_input):
    """Ask user to enter money and calculates if this amount enough and returns change if any"""
    print("Please Enter Coins.")
    quarters = int(input("How many Quarters? : "))
    dimes = int(input("How many Dimes? : "))
    nickles = int(input("How many Nickles? : "))
    pennies = int(input("How many Pennies? : "))
    total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if MENU[user_input]['cost'] > total_amount:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(total_amount - MENU[user_input]['cost'], 2)
    print(f"Here is ${change} dollars in change")
    return True


def make_coffee(user_input):
    """Update resources to make Coffee"""
    update_resources(user_input)
    print(f"Here is your {user_input} ☕ , Enjoy!!")


def _main_():
    """Main function for Coffee Machine"""
    print(logo)
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino) : ")
        if user_input == "off":
            break
        elif user_input == "report":
            print_report()
        else:
            if not valid_menu_item(user_input):
                print("Select Correct Menu Item..")
                continue
            elif not resources_available(user_input):
                continue
            elif not bill_check(user_input):
                continue
            else:
                make_coffee(user_input)


_main_()

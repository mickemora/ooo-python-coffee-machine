from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create a money_machine object
money_machine = MoneyMachine()

# Create a coffee_maker object
coffee_maker = CoffeeMaker()

# Create a menu object
menu = Menu()

# Set the is_on variable to True
is_on = True

# While the is_on variable is True
while is_on:
    # Call the get_items() method on the menu object and store the result in the items variable
    items = menu.get_items()

    # Call the get_user_choice() method on the menu object and store the result in the user_choice variable
    user_choice = input(f"What would you like? ({items}): ")

    # If the user_choice variable is equal to "off"
    if user_choice == "off":
        # Set the is_on variable to False
        is_on = False

    # Else if the user_choice variable is equal to "report"
    elif user_choice == "report":
        # Call the report() method on the coffee_maker object
        coffee_maker.report()

        # Call the report() method on the money_machine object
        money_machine.report()

    # Else
    else:
        # Call the find_drink() method on the menu object and pass in the user_choice variable as an argument and store the result in the drink variable
        drink = menu.find_drink(user_choice)

        # If the drink variable is not None
        if drink:
            # If the coffee_maker object's is_resource_sufficient() method returns True when passed the drink variable as an argument
            if coffee_maker.is_resource_sufficient(drink):
                # If the money_machine object's make_payment() method returns True when passed the drink variable's cost attribute as an argument
                if money_machine.make_payment(drink.cost):
                    # Call the make_coffee() method on the coffee_maker object and pass in the drink variable as an argument
                    coffee_maker.make_coffee(drink)
                    
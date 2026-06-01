# Object-Oriented Python Coffee Machine

This repository contains a command-line coffee machine simulator built with **Python** using an **object-oriented programming (OOP)** design.

The application lets a user order drinks, checks whether the coffee machine has enough resources, processes coin payments, tracks profit, and prepares the selected drink when all conditions are met.

## Project Overview

The project models a simple coffee machine that can serve the following drinks:

- Latte
- Espresso
- Cappuccino

Each drink has a defined ingredient requirement and cost. The program asks the user what they would like to order, verifies that the drink is available, checks whether there are enough machine resources, processes payment, and then dispenses the drink.

## Main Objective

The goal of this project is to practice **object-oriented programming in Python** by separating the coffee machine logic into dedicated classes.

Instead of placing all logic in one script, the project organizes responsibilities across multiple files and objects:

- `MenuItem` models an individual drink.
- `Menu` manages the available drink options.
- `CoffeeMaker` manages machine resources and prepares coffee.
- `MoneyMachine` handles payment, change, and profit tracking.
- `main.py` coordinates the application flow.

## Repository Structure

```text
.
├── main.py
├── menu.py
├── coffee_maker.py
├── money_machine.py
└── README.md
```

## Files and Responsibilities

### `main.py`

The main entry point of the application.

It creates instances of the main objects:

```python
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
```

The script then runs a loop that keeps the coffee machine active until the user enters `off`.

Supported user commands include:

- `latte`
- `espresso`
- `cappuccino`
- `report`
- `off`

Application flow:

1. Display available drink options.
2. Ask the user for a drink selection.
3. Turn off the machine if the user enters `off`.
4. Print a resource and money report if the user enters `report`.
5. Search for the selected drink in the menu.
6. Check whether resources are sufficient.
7. Process payment.
8. Make the coffee if payment is successful.

## `menu.py`

This file contains two classes: `MenuItem` and `Menu`.

### `MenuItem`

The `MenuItem` class models an individual drink item. Each menu item has:

- Name
- Cost
- Water requirement
- Milk requirement
- Coffee requirement

Example drink definitions include:

```python
MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)
```

### `Menu`

The `Menu` class stores the available drinks and provides methods to:

- Return all available drink names using `get_items()`
- Find a specific drink using `find_drink(order_name)`

If the requested drink is not available, the program prints:

```text
Sorry that item is not available.
```

## `coffee_maker.py`

The `CoffeeMaker` class models the machine that makes the coffee.

Initial machine resources are:

```python
self.resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
```

The class provides three main methods:

### `report()`

Prints the current available resources:

- Water
- Milk
- Coffee

### `is_resource_sufficient(drink)`

Checks whether the machine has enough resources to prepare the selected drink.

If an ingredient is insufficient, the program prints a message such as:

```text
Sorry there is not enough water.
```

### `make_coffee(order)`

Deducts the required ingredients from the machine resources and prints a confirmation message:

```text
Here is your latte ☕️. Enjoy!
```

## `money_machine.py`

The `MoneyMachine` class handles payment processing.

It supports the following coin types:

```python
COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}
```

The class tracks:

- Current profit
- Money received from the user

The class provides three main methods:

### `report()`

Prints the current amount of money earned by the machine.

### `process_coins()`

Prompts the user to enter the number of coins inserted and calculates the total amount received.

### `make_payment(cost)`

Checks whether the inserted money is enough to pay for the selected drink.

If payment is successful:

- Calculates change
- Adds the drink cost to profit
- Resets the money received
- Returns `True`

If payment is insufficient:

- Prints a refund message
- Resets the money received
- Returns `False`

## How the Program Works

The program follows this decision flow:

```text
Start machine
    ↓
Show available drinks
    ↓
Ask user for selection
    ↓
Is input "off"?
    → Yes: stop program
    → No: continue
    ↓
Is input "report"?
    → Yes: show resource and money report
    → No: continue
    ↓
Find selected drink
    ↓
Are resources sufficient?
    → No: show insufficient resource message
    → Yes: continue
    ↓
Process payment
    ↓
Is payment sufficient?
    → No: refund money
    → Yes: make coffee and deduct resources
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/mickemora/ooo-python-coffee-machine.git
```

2. Navigate into the project directory:

```bash
cd ooo-python-coffee-machine
```

3. Run the application:

```bash
python main.py
```

Depending on your environment, you may need to use:

```bash
python3 main.py
```

## Example Interaction

```text
What would you like? (latte/espresso/cappuccino/): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```

To see the machine status, enter:

```text
report
```

To turn off the machine, enter:

```text
off
```

## Key Programming Concepts Demonstrated

This project demonstrates several foundational Python and OOP concepts:

- Classes and objects
- Object instantiation
- Instance attributes
- Methods
- Encapsulation of responsibilities
- Conditional logic
- Loops
- Dictionaries
- Lists
- User input
- Basic arithmetic
- Program flow control
- Separation of concerns across multiple files

## Potential Enhancements

Possible future improvements include:

- Add input validation for coin entries
- Handle uppercase or mixed-case user input
- Add more drink options
- Add a refill resources feature
- Add automated tests
- Add type hints
- Add docstrings with more detailed examples
- Fix the coin label typo from `nickles` to `nickels`
- Add a graphical interface or web interface

## Summary

This project is a simple but useful Python exercise for practicing object-oriented design. It models a coffee machine using separate classes for the menu, drink items, machine resources, and payment processing. The project demonstrates how multiple objects can collaborate to support a complete command-line application.

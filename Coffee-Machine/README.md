# Coffee Machine

A simple command-line coffee machine program written in Python. This project is part of the 100 Days of Code challenge and simulates a basic coffee vending machine.

## Features

- Offers three types of coffee: Espresso, Latte, and Cappuccino
- Manages available resources (water, milk, coffee)
- Accepts money in quarters, dimes, nickels, and pennies
- Provides a report of available resources and total earnings
- Validates user input and ensures sufficient resources
- Calculates change if the user overpays

## How to Use

1. Run the script using Python.
2. Choose from `espresso`, `latte`, or `cappuccino`.
3. Insert coins when prompted.
4. The machine will check if there are enough resources.
5. If payment is sufficient, the coffee is served, and change is returned if needed.
6. Enter `report` to see the current resource status.
7. Enter `off` to turn off the machine.

## Installation

Make sure you have Python installed on your system.

1. Clone this repository:
   ```sh
   git clone https://github.com/nathanaelcheramlak/Python-Games.git
   ```
2. Navigate to the project folder:
   ```sh
   cd Python-Games/Coffee-Machine
   ```
3. Run the script:
   ```sh
   python coffee_machine.py
   ```

## Example Usage

```
What would you like? (espresso/latte/cappuccino): latte
How many quarters? 10
How many dimes? 0
How many nickels? 0
How many pennies? 0
latte has been served successfully.
Your change is: $7.50
```

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributions

Feel free to submit issues or pull requests to improve the coffee machine!

## Author

[Nathanael Cheramlak](https://github.com/nathanaelcheramlak)

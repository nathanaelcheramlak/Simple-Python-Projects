MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
totalMoneyGained = 0

def Query():
    query = ""
    while True:
        query = input("What would you like? (espresso/latte/cappuccino): ")
        if query == "off":
            break
        elif query == "report":
            report(resources)
        elif query in MENU.keys():
            global totalMoneyGained 
            totalMoneyGained += myCoffee(query)
        else:
            print("Invalid Input!")
    return 0

def report(resources):
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${totalMoneyGained:0.2f}")

def myCoffee(query):
    reqWater = MENU[query]["ingredients"]["water"]
    reqMilk = MENU[query]["ingredients"]["milk"]
    reqCoffee = MENU[query]["ingredients"]["coffee"]

    price = MENU[query]["cost"]
    resourceAvailable = reqCoffee <= resources["coffee"] and reqMilk <= resources["milk"] and reqWater <= resources["water"]
    if resourceAvailable:
        moneyAccepted = moneyCounter()
        if moneyAccepted < price:
            print(f"Sorry that's not enough money. Extra ${(price - moneyAccepted):0.2f} is required!")
            return 0
        resourceSubstractor(reqWater, reqMilk, reqCoffee)
        print(f"{query} has been served successfully.")
        print(f"Your change is: {changeCalculator(moneyAccepted, price):0.2f}")
        return price
    else:
        print("No enough resources. Come Again!")
        return 0

def moneyCounter():
    quarter = float(input("How many quarters? "))
    dime = float(input("How many dimes? "))
    nickel = float(input("How many nickels? "))
    penny = float(input("How many pennies? "))

    total = (quarter * 0.25) + (dime * .10) + (nickel * 0.05) + (penny * 0.01)
    return total

def resourceSubstractor(water, milk, coffee):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee

def changeCalculator(accptedMoney, price):
    return accptedMoney - price

Query()

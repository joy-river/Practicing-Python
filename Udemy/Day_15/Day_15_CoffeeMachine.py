from turtle import clear

from CoffeeMachineData import MENU, resources
import os

coffee_dic = {
    "input": "Which drink do you want to drink? (Espresso, Latte, Cappuccino) : "
}


def get_coin():
    quarter = int(input("How many quarters? : "))
    dime = int(input("How many dimes? : "))
    nickel = int(input("How many nickels? : "))
    penny = int(input("How many pennies? : "))
    return round(0.25 * quarter + 0.1 * dime + 0.05 * nickel + 0.01 * penny, 2)


def print_resource(money):
    print(
        f"Water : {resources['water']}ml\nMilk : {resources['milk']}ml\nCoffee : {resources['coffee']}g\nMoney : {money}$")


def check_ingredients(com, usage):
    ingredients = MENU[com]["ingredients"]
    if usage == 0:
        for key in ingredients:
            if resources[key] < ingredients[key]:
                print(f"Sorry, this machine run out of {key}")
                return False
        return True
    else:
        for key in ingredients:
            resources[key] -= ingredients[key]


def coffee(com, money):
    # os.system('clear')
    if com == "off":
        return
    if com == "report":
        print_resource(money)
        coffee(input(coffee_dic["input"]), money)
    else:
        if check_ingredients(com, 0):
            print("Insert your coin")
            coins = get_coin()
            if MENU[com]["cost"] > coins:
                print("Sorry that's not enough money. Your money has refunded. ")
                coffee(input(coffee_dic["input"]).lower(), money)
            else:
                check_ingredients(com, 1)
                print(f"Here's ${round(coins - MENU[com]['cost'], 2)} in change.")
                print(f"Here's your {com}! Enjoy!")
                coffee(input(coffee_dic["input"]).lower(), money + MENU[com]["cost"])
        else:
            coffee(input(coffee_dic["input"]).lower(), money)


coffee(input(coffee_dic["input"]).lower(), 0)

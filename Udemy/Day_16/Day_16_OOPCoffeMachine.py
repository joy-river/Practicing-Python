from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menus = Menu()
maker = CoffeeMaker()
casher = MoneyMachine()


def oopmachine():
    drink = input(f"Which drink do you want? Please type your order. : ").lower()
    if drink == "off":
        print("Good Bye.")
        return
    elif drink == "report":
        maker.report()
        casher.report()
    elif drink == "menu":
        print(f"{menus.get_items()}")
    else:
        drink = menus.find_drink(drink)
        if drink is not None:
            if maker.is_resource_sufficient(drink):
                if casher.make_payment(drink.cost):
                    maker.make_coffee(drink)

    oopmachine()
    return


oopmachine()

from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
Menu = Menu()
Coffee_Maker = CoffeeMaker()
Money_Machine = MoneyMachine()
is_on  = True


while is_on:
    options = Menu.get_items()
    print(f'These are the available items {options}')
    choice = input("Pls enter the drink you want:")
    if choice == "report":
        Coffee_Maker.report()
        Money_Machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = Menu.find_drink(choice)
        if Coffee_Maker.is_resource_sufficient(drink):
            print("this cost",drink.cost)
            if Money_Machine.make_payment(drink.cost):
                Coffee_Maker.make_coffee(drink)

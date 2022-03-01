from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isOff = False

menu = Menu()
coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()

while isOff == False:
    order = input(f"What drink would you like? {menu.get_items()}: ")
    if order == 'off':
        print("Machine is turning off.")
        isOff = True
    elif order == 'report':
        coffeeMachine.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(order)
        if coffeeMachine.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost) == True:
            coffeeMachine.make_coffee(drink)
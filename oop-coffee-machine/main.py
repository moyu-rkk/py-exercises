from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_on = True

while machine_on:

    order = input("What would you like?(espresso/latte/cappuccino):")

    MENU = Menu()
    new_coffee_maker = CoffeeMaker()
    new_money_machine = MoneyMachine()
    #所以你一开始为啥要用跟class一样的名字做variable名，所以就会报错惹……提示is not callable，故意来耍电脑的吧
    #TypeError: Missing 1 required positional argument: 'self'
    #引入class以后，需要先instantiate一个object出来，不能直接拿blueprint来用

    if order in MENU.get_items():
        order = MENU.find_drink(order)
        if new_coffee_maker.is_resource_sufficient(order):
            if new_money_machine.make_payment(order.cost):
                new_coffee_maker.make_coffee(order)

    elif order == "report":
        new_coffee_maker.report()
        new_money_machine.report()

    elif order == "off":
        machine_on = False



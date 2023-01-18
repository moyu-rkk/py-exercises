# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:41:15 2022

@author: robin
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "coffee": 100
}


money = {"income" : 0,
         "change": 0
}


def coffee_order():
    
    order = input("What would you like?(espresso/latte/cappuccino):")

    if order.lower() == "espresso":
        return "espresso"
    elif order.lower() == "latte":
        return "latte"
    elif order.lower() == "cappuccino":
        return "cappuccino"
    elif order.lower() == "report":
        return "report"
    elif order.lower() == "off":
        return "off"


def check_stock(coffee, menu, resources):
    
    water_msg = "Sorry there is not enough water."
    milk_msg = "Sorry there is not enough milk."
    coffee_msg = "Sorry there is not enough coffee."
    
    if water_stock >= water_need and milk_stock >= milk_need and coffee_stock >= coffee_need:
        return True
    elif water_stock < water_need:
        print(water_msg)
        return False
    elif milk_stock < milk_need:
        print(milk_msg)
        return False
    elif coffee_stock < coffee_need:
        print(coffee_msg)
        return False

#可以用for loop写
        
def stock_update(stock, need):
    return stock - need


def inserted_coins(coffee, menu, money):
    
    print("Please insert coins.")
    
    quarters = float(input("How many quarters:"))
    dimes = float(input("How many dimes:"))
    nickles = float(input("How many nickles:"))
    pennies = float(input("How many pennies:"))
    
    total_coins = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    coffee_price = menu[coffee]["cost"]
    
    if total_coins == coffee_price:
        return True, round(total_coins, 2), 0
    elif total_coins > coffee_price:
        change = round(total_coins - coffee_price, 2)
        print(f"Here is ${change} in change.")
        return True, round(total_coins, 2), change
    elif total_coins < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        return False, 0, 0
    
#一个function负责一个环节/判断，最好不用混用，回头比较好改，也比较好梳理在流程中负责的逻辑环节
    
machine_on = True

while machine_on:
    
    choice = coffee_order()
    
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        
        water_need = MENU[choice]["ingredients"]["water"]
        milk_need = MENU[choice]["ingredients"]["milk"]
        coffee_need = MENU[choice]["ingredients"]["coffee"]
        
        water_stock = resources["water"]
        milk_stock = resources["milk"]
        coffee_stock = resources["coffee"]
        
        is_available = check_stock(choice, MENU, resources)
        
        if is_available:
            is_paid = inserted_coins(choice, MENU, money)
            if is_paid[0]:
                print(f"Here is your {choice}. Enjoy!")
                
                resources["coffee"] = stock_update(coffee_stock, coffee_need)
                resources["milk"] = stock_update(milk_stock, milk_need)
                resources["water"] = stock_update(water_stock, water_need)
                #这个更新库存环节可以另外写一个function出来
                
                money["income"] += is_paid[1]
                money["change"] -= is_paid[2]
    #这里不用放continue欸，之前多余了，他会继续运行的，不满足的话就跳到下一个elif，因为loop进行的条件是machine_on是True
    
    elif choice == "report":
        repo = f"""Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money['income']}"""
        print(repo)
        continue
        
    elif choice == "off":
        machine_on = False

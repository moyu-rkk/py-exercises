# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 23:54:39 2021

@author: robin
"""
#from replit import clear

auction = {}

flag = True

while flag:
    buyer = input("Please enter your name:\n")
    price = int(input("How much will you like to pay?\n"))
    check = input("Is there any other bidder?Enter 'yes' or 'no'.\n")


    auction[buyer] = price
    
# =============================================================================
#     if check.lower()=="yes":
#         clear()
# =============================================================================
    if check.lower() == "no":
        flag = False
        
compare_price = auction.values()

top_price = max(compare_price)

for i, v in auction.items():
    if top_price == v:
        winner = i
        
print(f"The winner is {winner}.")

#迭代的时候直接引用dict会raise ValueError: too many values to unpack (expected 2)
#还差清屏功能和一些user friendly的improvement



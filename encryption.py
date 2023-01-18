# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 23:17:55 2021

@author: robin
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# =============================================================================
# def encrypt(text, interval):
#     result = []
#     for chara in text.lower():
#         place = letters.index(chara)
#         change = place + int(interval)
#         if change > 25:
#             change -= 26
#         result.append(letters[change])
#     
#     print("".join(result))
#         
# 
# def decrypt(text, interval):
#     result = []
#     for chara in text.lower():
#         place = letters.index(chara)
#         change = place - int(interval)
#         result.append(letters[change])
#     
#     print("".join(result))
# =============================================================================
    
def ceasar(text, shift_amount, cipher_direction):
    result = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    #如果不小心把这个判断放进for loop就会出现shift amount左右横跳，因为decode成立的情况下，每次循环都会执行*-1的操作
    for char in text:
        if char in letters:
            position = letters.index(char)
            new_position = position + int(shift_amount)
            result += letters[new_position]
        else:
            result += char
    print(f"Here's the {cipher_direction}d result: {result}")

should_end = False

while not should_end:
    
    msg = input("Give me your message:\n")
    shift = int(input("Give me the amount you wanna shift:\n"))
    direction = input("Would you like to encrypt or decrypt. Type 'encode' or 'decode' to confirm.\n")
    
    shift = shift%26

    ceasar(msg, shift, direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")


#除了取26的余数，还有个最简单的办法，在z后面再接一串26字母……妙蛙种子
#angela蛮喜欢直接用bool做flag的，很直观的开关
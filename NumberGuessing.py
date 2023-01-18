# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:07:55 2022

@author: robin
"""
#1、学会使用全局变量，特别是做游戏开发的时候，数值作为全局变量来引用比较保险
#2、学会模块化，善用def，之前blackjack也可以用def优化，比如check的时候，有需要更新和追踪的数值可以放到return里引用

import random

TURNS_EASY_LEVEL = 10
TURNS_HARD_LEVEL = 5

def set_difficulty():
    count = 0
    level = input("Choose a difficulty. Enter 'hard' or 'easy':")

    if level.lower() == 'hard':
        count = TURNS_HARD_LEVEL
    elif level.lower() == 'easy':
        count = TURNS_EASY_LEVEL
    return count

def check(num, user_num, turns):
    if num > user_num:
        print('Too low.Guess again.')
        turns -= 1
    elif num < user_num:
        print('Too high.Guess again.')
        turns -= 1
    elif num == user_num:
        print('You got it!')
    return turns

def Number_Guessing():
    
    print("""
          Welcome to the Number Guessing Game!\n
          I'm thinking of a number between 1 and 100.
          """)

    turns = set_difficulty()
    num = random.choice(range(1,101))#==randint(1, 100)
    user_num = 0
        
    while num != user_num:
        
        print(f"You have {turns} attempts to guess the number.\n")
        
        user_num = int(input("Give me your number:"))
        turns = check(num, user_num, turns)
        
        if turns == 0:
            print("You've run out of attempts. You lose.")
            break
    
    new_game = input("\nWould you like to start a new game? Enter 'y' or 'n':")
    
    if new_game == 'y':
        Number_Guessing()
    else:
        return

Number_Guessing()

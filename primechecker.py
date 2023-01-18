# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 23:44:41 2021

@author: robin
"""


def primechecker(x):
    is_prime =True
    for i in range(2, x):
        if x % i == 0:
            is_prime =False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")
            
            
primechecker(7)
primechecker(10)

#其实一开始直觉的思路就感觉要除到9……
#如果直接在循环中放是否质数的结论，那每loop到一个数就会打印一次……
#如果把初始设定的flag放在loop中，如果遇到可除数的时候不打断循环，设置的flag就会以最后一个被除数的判断为准，然后就会变成都是质数，x/(x-1)是除不尽的
#但是如果把flag放在loop外面就不会，一旦符合条件flag改变，后续就不会再改变了——因为等于true的条件被放在loop外，只要一个除得尽，flag turn false以后就没有机会变回true了啊！
#range(x, x)是个空集，所以如果input是2，会直接跳过for loop，不会出现bug
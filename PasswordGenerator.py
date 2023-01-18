# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 23:14:25 2021

@author: robin
"""


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

result = []

for i in range(nr_letters):
    result.append(random.choice(letters))
    
for i in range(nr_symbols):
    result.append(random.choice(symbols))

for i in range(nr_numbers):
    result.append(random.choice(numbers))
    
random.shuffle(result)

print("".join(result))#join是把list转变为string


#str不能将list转化为string，只能作用于int,float,bool？

#randrange的变量只能是int，是在两个数字组成的区间内随机选择一个数字，list进去会报错
#而choice可以实现从一个非空sequence for example a list里随机选择一个元素，空集会raise IndexError

#TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
#int()可以实现①把string类型的整数变成int；②把带小数点的数字变为整数（直接切掉尾巴，round才可以四舍五入）
#('float'/str(float))放进去会raise ValueError: invalid literal for int() with base 10: '32.5'
#(float, base)会raise TypeError: int() can't convert non-string with explicit base
#('float'/str(float), base)会raise ValueError: invalid literal for int() with base 2: '32.5'
#所以base是不可改动的参数- -
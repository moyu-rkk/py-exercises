# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:27:08 2021

@author: robin
"""


import json
from difflib import get_close_matches

data = json.load(open("C:\\Users\\robin\\Desktop\\data.json"))

def trans(word):
    word = word.lower()
    if word in data:
        return data.get(word)
    elif len(get_close_matches(word, data.keys())) > 0:
        retry= input(
            "Did you mean %s instead? Enter Y/N to comfirm: " 
            % get_close_matches(word, data.keys())[0]
            )
        if retry == "Y":
            return data.get(get_close_matches(word, data.keys())[0])
        if retry == "N":
            return "残念"
        else:
            return "You are not allowed to input other than 'Y' or 'N'. Try again."
    else:
        return "The word doesn't exist. Please double check it."
    
word = input("Enter word:")

result = trans(word)

if type(result) == list:
    serial = 0
    for i in result:
        serial += 1
        print("%d. " %serial + result[serial -1])
else:
    print(result)
    
    


#输出优化放在方法域之外，因为在方法内用return返回结果，多个结果只会返回第一个；如果在方法域内使用循环打印结果，最后还会返回一个None
#优化了有输出返回的情况，不要忘了其他情况还要打印结果……用新变量储存调用方法以后的返回值，再次直接调用方法会各种报错（（（
#优化需求：1、词是正确的，词库没有收录，如何识别词是正确、存在的？如何添加到词库？2、识别缩写
    
    
    
# =============================================================================
# runfile('C:/Users/robin/未命名0.py', wdir='C:/Users/robin')
# 
# Enter word:tech
# 
# Did you mean teach instead? Enter Y/N to comfirm: N
# 
# runfile('C:/Users/robin/未命名0.py', wdir='C:/Users/robin')
# 
# Enter word:tech
# 
# Did you mean teach instead? Enter Y/N to comfirm: Y
# Traceback (most recent call last):
# 
#   File "C:\Users\robin\未命名0.py", line 38, in <module>
#     for i in data.get(word):
# 
# TypeError: 'NoneType' object is not iterable
# 
# 
# runfile('C:/Users/robin/未命名0.py', wdir='C:/Users/robin')
# 
# Enter word:tech
# 
# Did you mean teach instead? Enter Y/N to comfirm: N
# 
# runfile('C:/Users/robin/未命名0.py', wdir='C:/Users/robin')
# 
# Enter word:tech
# 
# Did you mean teach instead? Enter Y/N to comfirm: N
# 
# Did you mean teach instead? Enter Y/N to comfirm: Y
# ['To pass on knowledge and skills.']
# 
# runfile('C:/Users/robin/未命名0.py', wdir='C:/Users/robin')
# 
# Enter word:tech
# 
# Did you mean teach instead? Enter Y/N to comfirm: N
# 残念
# 
# runfile('C:/Users/robin/未命名0.py', wdir='C:/Users/robin')
# 
# Enter word:tech
# 
# Did you mean teach instead? Enter Y/N to comfirm: Y
# Traceback (most recent call last):
# 
#   File "C:\Users\robin\未命名0.py", line 35, in <module>
#     for i in data.get(word):
# 
# TypeError: 'NoneType' object is not iterable
# 
# 
# runfile('C:/Users/robin/未命名0.py', wdir='C:/Users/robin')
# 
# Enter word:tech
# 
# Did you mean teach instead? Enter Y/N to comfirm: Y
# Traceback (most recent call last):
# 
#   File "C:\Users\robin\未命名0.py", line 37, in <module>
#     print("%d. " %serial + data.get(word)[serial -1])
# 
# TypeError: 'NoneType' object is not subscriptable
# =============================================================================

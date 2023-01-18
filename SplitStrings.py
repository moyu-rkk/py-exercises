# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:24:36 2022

@author: robin
"""

def solution(s):
    
    str_pieces = []
    str_len = int(len(s))
    
    if str_len%2 == 1:
        s += '_'
        str_len += 1
    
    for i in range(str_len//2):
        str_pieces.append(s[2*i: 2*(i+1)])
        
    return str_pieces



s = "asdfadsf"

print(solution(s))

#切片问题，本质上是首尾index的函数问题
#切片的时候，可以正负index混用
#AttributeError: 'str' object has no attribute 'append'
#等等，你怎么看题的，他也没要求从后面开始截起啊。。。。。。你按顺序截不就好了
#是我擅自把难度加大了；只要把index的函数改一下就可以了- -

#压缩到一行代码只是语法上的炫技操作罢惹，本质只是函数问题
#def solution(s):
#    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]
#loop的时候也可以规定步数，这样直接loop 0，2，4，6，8
#但是这个解法他怎么判断字符串长度是否为双数或者0的- -
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 23:49:46 2021

@author: robin
"""


def is_square(n):
    result = False
    
    high = n
    low = 0
    
    if n > 0:
        while high - low > 1:
            middle = int((high+low)/2)
            if middle**2 == n:
                result = True
                break
            elif middle**2 > n:
                high = middle
            elif middle**2 <n:
                low = middle
    elif n == 0:
        result = True
                
    return result


print(is_square(68))

#def is_square(n):
#    return n >= 0 and (n**0.5)%1 == 0
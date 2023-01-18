# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:41:37 2021

@author: robin
"""

def persistence(n):
    temp = n
    count = 0
    digits = len (str (n))
    
    if digits > 1:
        while digits > 1:
            var = 1
            for i in str (temp):
                var *= int (i)
            temp = var
            digits = len (str(var))
            count += 1
            
    return count


print(persistence(1218))
print(persistence(1025))
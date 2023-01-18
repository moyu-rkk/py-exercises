# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 00:08:16 2021

@author: robin
"""

def make_readable(seconds):
    if seconds <= 359999:
        ss = str(int(seconds % 60))
        mm = str(int((seconds/60)%60))
        hh = str(int((seconds/3600)%100))
            
    return f"{hh.zfill(2)}:{mm.zfill(2)}:{ss.zfill(2)}"


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))

#不用round的原因，内置运算本身有问题，会产生浮点，int可以直接chop掉
#判断好像有点多余，题目没要求做proof，而且也只是做了一半，没有错误提示（
#zfill原来是zerofill的意思嗷！学会用惹！
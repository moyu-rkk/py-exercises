# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 23:33:52 2021

@author: robin
"""


def longest_piece(s):
    piece = ""
    result = ""
    start_place = 0
    end_place = 0
    
    for char in s:
        end_place += 1
        if char not in piece:
            piece = s[start_place:end_place]
            if len(piece) > len(result):
                result = piece
        else:
            rev = piece[::-1]
            start_place = end_place - rev.index(char) - 1
            piece = ""
            piece = s[start_place:end_place]
                
            continue
    
    print(result, len(result))
    
    
longest_piece("abacabcedf")
longest_piece("abcabcbb")
longest_piece("bbbbbbb")
longest_piece("pwwkew")
longest_piece("")


#v3.0，第一版直接在重复处打断，忽略往前找；第二版如果字母重复第三次就出bug，裂开
#index用成方括号[]，会raise TypeError: 'builtin_function_or_method' object is not subscriptable
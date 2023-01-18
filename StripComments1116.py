# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:50:35 2022

@author: robin
"""

def strip_comments(strng, markers):
    
    txt = strng.splitlines()

    for m in markers:
        for item in txt:
            if m in item:
                edpt = item.index(m) 
                newitem = item[0:edpt].rstrip()
                txt[txt.index(item)] = newitem
    
    return "\n".join(txt)



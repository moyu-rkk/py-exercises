# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 20:45:36 2022

@author: robin
"""

def move_zeros(lst):
    
    nullappear = 0
    items = len(lst)
    
    while items > 0:
        items -= 1
        if 0 in lst:
            nullappear += 1
            lst.remove(0)
            lst.append(0)
            
            print(lst)
    
    return lst


lst = [1, 0, 1, 2, 0, 1, 3]
print(move_zeros(lst))


#both remove() and append() modify the original list
#when putting zeros at the end, every time they're removed they get appended immediately

#looks like for loops save space than while loop
#每次要引入计数的时候就可以考虑改用for loop，while比较适合有边界条件switch between True and False

# =============================================================================
# def move_zeros(array):
#     for i in array:
#         if i == 0:
#             array.remove(i) # Remove the element from the array
#             array.append(i) # Append the element to the end
#     return array
# =============================================================================

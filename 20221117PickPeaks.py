# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 18:04:52 2022

@author: robin
"""

def pick_peaks(arr):
    
    pos = []
    peaks = []
    
    interval = len(arr)-1

    for i in range(1,interval):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            pos.append(i)
            peaks.append(arr[i])
        elif arr[i] > arr[i-1] and arr[i] == arr[i+1]:
            for j in range(i,interval):
                if arr[j] == arr[i] and arr[j] > arr[j+1]:
                    pos.append(i)
                    peaks.append(arr[i])
                    break
                elif arr[j] < arr[j+1]:
                    break
    
    return {"pos":pos, "peaks":peaks}
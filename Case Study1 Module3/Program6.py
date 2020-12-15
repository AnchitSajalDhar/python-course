# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:57:07 2020

@author: Hp
"""

list1=[]
for i in range(2000,3200+1):
    if i %7==0 and i %5!=0:
        list1.append(i)
print(list1)
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 22:04:14 2020

@author: Hp
"""
import math
c,h=50.0,30.0
list1=[]
d=(input("enter the number for sqrt"))
h1=list(d.split(","))
for i in h1:
    
    x1=((2*c*int(i))/h)
    x=int(math.sqrt(x1))
    list1.append(x)
print(list1)

    
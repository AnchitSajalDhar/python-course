# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:33:35 2020

@author: Hp
"""

num=int(input("enter the number for which series need to be generated"))
x=1
sum1=0
y=0
for i in range(2,num+2):
    sum1= x/i
    x+=1
    print("the value is %d", sum1)
    y+=sum1
print(y)
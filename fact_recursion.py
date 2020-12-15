# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 07:30:48 2020

@author: Hp
"""


def fact1(a):
    if a==0:
        return 1
    else: 
     return a* fact1 (a-1)
n=int(input("enter the number for factorial"))
x=fact1(n)
print(x)
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:38:20 2020

@author: Hp
"""
list2=[]
while True:
    
    str1=input("enter the sequence of words with comma seperation")
    if str1:
        list2.append(str1.upper())
    else:
        break
    
print(list2)
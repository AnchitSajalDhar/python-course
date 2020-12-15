# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:52:46 2020

@author: Hp
"""
list2=[]
str2=""
str1=input("enter the sequence of words with comma seperation")
list1=str1.split()
for i in list1:
    if i not in list2:
        list2.append(i)
        
for i in list2:
    str2+=i
print(str2.join(""))
        
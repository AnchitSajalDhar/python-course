# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 22:35:09 2020

@author: Hp
"""
str2=""
str1=input("enter the string")
for i in str1:
    str2=i+str2
print(str2)
for i in str1:
    print(str1.index(i))
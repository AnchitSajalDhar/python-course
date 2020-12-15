# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 12:44:28 2020

@author: Hp
"""

str1=input("\n enter the number")
list1=list(str1.split())
str2=input("\n enter the number to be removed from the list")
for i in (list1):
    if str(i)== str2:
        list1.remove(str2)
print(list1)
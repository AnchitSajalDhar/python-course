# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 23:15:41 2020

@author: Hp
"""

str1 = input("Enter a string: ")



str2 = ''
for i in str1:
    if i not in str2:
        print(i, ', ', str1.count(i))
        str2+=i
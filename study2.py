# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:18:23 2020

@author: Hp
"""

str1=input("input the string to be reversed")
word=str1.split()
word.sort()
#str1.sort()
print(str1)
print("the sorted string is ")
for i in word:
    print(i)

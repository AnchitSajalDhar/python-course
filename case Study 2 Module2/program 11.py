# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:17:07 2020

@author: Hp
"""


str1=input("\n enter the number")
list1=list(str1.split())
for i in list1:
     if (int(i) %5==0 or int(i) %7 ==0):
         list1.remove(i)

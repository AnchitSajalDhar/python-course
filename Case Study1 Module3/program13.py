# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:00:14 2020

@author: Hp
"""
list2=[]
str1=input("enter the 4 digit binary code sperated by comma")
list1=list(str1.split(","))
for i in list1:
    bin1=int(i,2)
    if (bin1 % 5 ==0):
        list2.append(i)
print(list2)
        
        
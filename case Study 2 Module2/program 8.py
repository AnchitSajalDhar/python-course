# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 12:07:05 2020

@author: Hp
"""

str1=(input("enter the list1"))
#list13=[1,3,6,78,35,55]

str2=(input("enter the list1"))


list1=list(str1.split())
list2=list(str2.split())
#list3=[]
list3=list(set(list1) & set(list2))
print("intersection of list", list3)




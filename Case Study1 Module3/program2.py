# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:08:17 2020

@author: Hp
"""

n=input("enter the elements in the list")
list1=list(n.split())
list1.sort()
#list2=list(n.sort())
search=input("the element to be searched")
for i in list1:
    if i==search:
        flag=1
        
if flag==1:
    print("element found")
else:
    print("element not found")
    
        
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:30:27 2020

@author: Hp
"""
count=0
list1=list(input("enter the elements in the list"))
for i in list1:
    
    print(count,",",i)
    count+=1
    #using Enumaration 
for i, val in enumerate(list1): 
        print (i, ",",val) 
        

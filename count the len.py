# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:53:59 2020

@author: Hp
"""
count=0
x=(input("enter the number to count the number of digit"))
n=int(x)
while(n>0):
  count+=1
  n//=10
print(count)

x=len(x)
print(x)
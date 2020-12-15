# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:41:17 2020

@author: Hp
"""
f=1
i=1
n=int(input("enter the number for caluclating factorial"))
#while(i<=n)
for i in range(1,n+1):
    f*=i
    #i+=1
print("the factorial is ",f)


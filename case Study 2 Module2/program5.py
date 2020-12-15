# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:39:32 2020

@author: Hp
"""

str1=input("enter the string")
len1=len(str1)
str2=""


for i in str1:
    if str1.index(i)%2==0 :
        str2+=str(i)
       
print(str2)


for i in str1:
    print(str1.index(i))

str3 = str1[::2]
print(str2)
        

    
    
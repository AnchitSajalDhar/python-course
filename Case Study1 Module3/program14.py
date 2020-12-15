# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:11:25 2020

@author: Hp
"""

str1=input("enter the string")
count1,count2=0,0

for i in str1:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)
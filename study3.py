# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:35:27 2020

@author: Hp
"""


list1=[]
for i in range(1000,3001):
    if(i%2==0):
      #  print("\t %d"%i)
       list1.append((i))
#for x in list1:
print(list1)

nums =set([1,1,2,3,3,3,4,4])
print(len(nums))

d ={"john":40, "peter":45}
print(list(d.keys()))
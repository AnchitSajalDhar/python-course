# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:20:16 2020

@author: Hp
"""

import pandas
list1=[]
#str1=input("enter the profession")

pd=pandas.read_csv("bank-data.csv")
len1=len(pd.job)
print(pd)
#print(pd)
for i in range(len1):
    if (pd.job[i]) not in list1:
         list1.append(pd.job[i])


print(list1)

flag=0
str1=input("enter the profession")    
for i in list1:
    if i==str1:
        flag=1
            
if flag==1:
    
        print("data exist")
else:
        print("data doesnt exist")
flag=0
'''for i in list1 :
    if (str1==list1[0] or str1==list1[8] or str1==list1[2]):
        flag=1
if flag==1:
    
        print("not eligible for loan")
else:
        print("suitable for loan")
   '''     
for i in range(len1):
    if pd.job[i]== list1[0] or pd.job[i]==list1[2] or pd.job[i]==list1[8]:

        print(pd.job[i],pd.age[i],"not eligible for loan")
        'print("not eligible for loan")'
    else:
        print(pd.job[i],pd.age[i],"eligible for loan")
       
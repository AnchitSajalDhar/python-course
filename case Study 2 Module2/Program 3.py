# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:09:01 2020

@author: Hp
"""

import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")

l, u, p, d = 0, 0, 0, 0
s = input("Input Yout Password")
if (len(s) >6 or len(s)<12): 
    for i in s: 
  
      
        #print(i)   
        if (i.islower()): 
            l+=1            
  
        if (i.isupper()): 
            u+=1            
  
       
        if (i.isdigit()): 
            d+=1            
  
       
        if(i=='$'or i=='#' or i=='@'): 
            p+=1           
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)): 
    print("Valid Password") 
else: 
    print("Invalid Password") 
    
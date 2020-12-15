# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:04:49 2020

@author: Hp
"""
from cryptography.fernet import Fernet
refid=input("enter the refrence id ")
l, u, p, d = 0, 0, 0, 0
#s = input("Input Yout Password")
if (len(refid) ==12): 
    for i in refid: 
  
      
        #print(i)   
        if (i.islower()): 
            l+=1            
  
        if (i.isupper()): 
            u+=1            
  
       
        if (i.isdigit()): 
            d+=1            
  
       
        if(i=='$'or i=='#' or i=='@'): 
            p+=1     
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(refid)): 
          print("password is valid")
         # from cryptography.fernet import Fernet
          key = Fernet.generate_key()#data storing in file
          file = open('key.key', 'wb')
          file.write(key)
          file.close()
          s1=refid.encode() #encoding the string in binary
          #print(s1)
          f=Fernet(key)
          s2=f.encrypt(s1)#encryption 
          print(s2)
          s3=f.decrypt(s2)
          print("content saved in key file")
          file=open("key.key","rb")
          for i in file:
            #  file.readline(i)
              print(i)    
             # key=file.read()
          file.close()
          
          
          
else:
    print("the refrene id is false try again")
    
#
    
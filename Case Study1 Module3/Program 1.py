# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:30:42 2020

@author: Hp
"""
import math
Move=input("enter the Movment of robot")
x,y=0,0
move=list(Move.split())
for i in move:
    if Move=="":
        break
    else:
       # move=Move.split(" ")
       

        if int(i)==5:
           y=y+1
        elif int(i) == 3:
            y=y-1
        elif int(i) == 7:
            x -=1 
        elif int(i)== 2:
            x +=1 

c = math.sqrt(x**2 + y**2)

print("Distance:", c)
print("the co-ordinate value of x=",x,"the co-ordinate value of y=",y)
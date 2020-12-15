# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:17:42 2020

@author: Hp
"""
from math import sin,cos,sqrt,atan2
import math
R = 6373.0
lat1=math.radians(float (input("enter the latitude 1")))
lon1=math.radians(float(input("enter the longitude 1")))
lat2=math.radians(float (input("enter the latitude 2")))
lon2=math.radians(float(input("enter the longitude 2")))
dlon = lon2 - lon1
dlat = lat2 - lat1
a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
distance = (R* c)
print("the distance between the two co-ordinates are:",distance,"km")


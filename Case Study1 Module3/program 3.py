# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:34:49 2020

@author: Hp
"""

import time
localtime = time.localtime()
print(localtime)

mytime = time.localtime()
if mytime.tm_hour < 12:
    print ('It is AM')
else:
    print ('It is PM')
    


if mytime.tm_hour < 6 or mytime.tm_hour > 18:
    print ('It is night-time')
else:
    print ('It is day-time')
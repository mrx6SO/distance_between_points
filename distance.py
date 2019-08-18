#!/usr/bin python 

# -*- coding: utf-8 -*- 

import math

x=input() # 1 
y=input() # 1 

x_=input() # 4 
y_=input() # 1 

# Fórmula usada para estabelecer entre dois pontos distintos. (x1,x2) e (y1,y2)

# dAB = \/(x1-x2)^2 + (y1 - y2) ^2 

result = (math.sqrt(x-y)**2 + (x_-y_)**2)

result_ = math.sqrt(result) 

print result_ # 3 

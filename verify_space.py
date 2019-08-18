#!/usr/bin python 

# -*- coding: utf-8 -*- 

import math, random

def distance_betw_point():


        result = math.sqrt(x-y)**2 + (x_-y_)**2

        result_ = math.sqrt(result) 
            
        print result_ 
        
def verify_space_dimensional():
	
  # compare the vectors to assign the dimension that's been worked out 
  # if the tuple(x,y) is not equal to tuple (x_,y_) then we're working in bi-dimension. 
  
	space_bi_dim = (x,y) != (y_,x_)
	
	print space_bi_dim 

if __name__ == "__main__":
    
    x=input() # 1 
    y=input() # 1 

    x_=input() # 4 
    y_=input() # 1 
   
    
    distance_betw_point()
    verify_space_dimensional()

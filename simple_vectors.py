#!/usr/bin python
# -*- coding: utf-8 -*- 

import math

def check_vector():

    ''' 
       v = B - A 
    '''

    vec = b-a

    print vec 

def vector_module():

    ''' 
       v = (a,b) 

    ''' 

    module_vec = math.sqrt(a**2+b**2) 

    print module_vec 


    pass


def vector_uni():

    vector_u = (b-a)/(math.sqrt(a**2+b**2)) 

    
    print vector_u 

if __name__ == "__main__":

    a=input("value of segment A: ")
    b=input("value of segment B: ")

    check_vector()

    vector_module()
 
    vector_uni()

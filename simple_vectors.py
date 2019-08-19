#!/usr/bin python
# -*- coding: utf-8 -*- 

import math
import numpy as np

def check_vector():

    ''' 
       v = B - A 
    '''

    vec = b - a

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


def distance_betw_point():


    result = math.sqrt(a-b)**2 + (c-d)**2

    result_ = math.sqrt(result) 
            
    print result_ 


def build_basic_vec():

    '''
      v = (1,0) 
    '''
    print "v = ", (a,b)
    print "w = ", (c,d)

def sum_of_vect():

    '''
       v + w = (a+c,b+d)
    '''

    vect_sum = (a+c,b+d)

    print vect_sum 

if __name__ == "__main__":

    a=input("value of segment A: ")
    b=input("value of segment B: ")

    c=input()
    d=input()

    check_vector()

    vector_module()

    vector_uni()

    distance_betw_point()
    build_basic_vec()

    sum_of_vect()

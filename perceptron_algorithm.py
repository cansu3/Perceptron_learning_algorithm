# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 02:18:19 2022

@author: cansu
"""

import numpy 
from numpy import random
import activation_functions as af


def perceptron_learning_algorithm_with_hardlims(p,t):
    
    p_rows, p_cols = p.shape #find the row and column numbers of the matrix
    
    p_split=numpy.array(numpy.hsplit(p,p_cols)) #split the matrix into columns
    
    w = (random.rand(p_rows)-0.5)*2 #random values between 1 and -1
    b = (random.rand()-0.5)*2
    
    
    number_of_true_output = 0
    
    while number_of_true_output < p_cols: #keep looping until all outputs are correct
        
        number_of_true_output = 0
        
        for i in range(p_cols):
            
            a = af.hardlims((w.dot(p_split[i])+b).__float__()) #use hardlims function and calculate output
            e = t[i]-a #calculate error
            w = w + (p_split[i]).transpose()*e #calculate new weight
            b = b+e #calculate new skaler number
            
            if e==0:
                number_of_true_output+=1 #increase the number of correct outputs
                
            print("number:",i)
            print("p: ",p_split[i])
            print("t: ",t[i])
            print("a:",a)         
            print("e: ",e)
            print("w: ",w)   
            print("b: ",b)
            print('---------------------------')
            
def perceptron_learning_algorithm_with_hardlim(p,t):
    
    p_rows, p_cols = p.shape 
    
    p_split=numpy.array(numpy.hsplit(p,p_cols)) 
    
    w = (random.rand(p_rows)-0.5)*2 
    b = (random.rand()-0.5)*2
    
    
    number_of_true_output = 0  
    
    while number_of_true_output < p_cols: 
        
        number_of_true_output = 0
        
        for i in range(p_cols):
            
            a = af.hardlim((w.dot(p_split[i])+b).__float__()) ##use hardlim function
            e = t[i]-a 
            w = w + (p_split[i]).transpose()*e
            b = b+e
            
            if e==0:
                number_of_true_output+=1
                
            print("number:",i)
            print("p: ",p_split[i])
            print("t: ",t[i])
            print("a:",a)         
            print("e: ",e)
            print("w: ",w)   
            print("b: ",b)
            print('---------------------------')
               
    
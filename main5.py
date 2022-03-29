# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:56:21 2022

@author: cansu
"""
import perceptron_algorithm as pa
import numpy 


p=numpy.array([(-1, -1, -1, -1,  1 , 1,  1  ,1),  #Parite 3 Problem
    (-1, -1 , 1,  1 ,-1, -1 , 1,  1),
    (-1,  1, -1,  1, -1,  1, -1 , 1)])
t=numpy.array([-1 , 1 , 1 ,-1 , 1, -1, -1, 1])

pa.perceptron_learning_algorithm_with_hardlims(p, t)

#can't learning




# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:42:19 2022

@author: cansu
"""

import perceptron_algorithm as pa
import numpy 


p=numpy.array([(2, 1, -2, 1),(2, -2 , 2,  1)]) #test
t=numpy.array([0 , 1 , 0 ,1])

pa.perceptron_learning_algorithm_with_hardlim(p, t)

#learning successfully

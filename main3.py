# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:52:48 2022

@author: cansu
"""

import perceptron_algorithm as pa
import numpy 


p=numpy.array([(0, 0, 1, 1),(0, 1 , 0,  1)]) #OR
t=numpy.array([0 , 1 , 1 ,1])

pa.perceptron_learning_algorithm_with_hardlim(p, t)

#learning successfully
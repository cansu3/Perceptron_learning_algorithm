# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:46:41 2022

@author: cansu
"""

import perceptron_algorithm as pa
import numpy 


p=numpy.array([(0, 0, 1, 1),(0, 1 , 0,  1)]) #AND
t=numpy.array([0 , 0 , 0 ,1])

pa.perceptron_learning_algorithm_with_hardlim(p, t)

#learning successfully
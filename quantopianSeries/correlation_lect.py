# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:27:43 2016

@author: callejal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


X = np.random.rand(50)
Y = 2* X + np.random.normal(0,0.1,50)

np.cov(X,Y)[0,1]

X= np.random.rand(50) #returns an array
Y = 2*X+4

print('Covariance of X and Y: \n' + str(np.cov(X,Y)))
print('Correlation of X and Y: \n' + str(np.corrcoef(X,Y)))

cov_matrix = np.cov(X,Y)
error = cov_matrix[0,0] - X.var(ddof=1)
print('error: ' + str(error))

X = np.random.rand(50)
Y = np.random.rand(50)
plt.scatter(X,Y)
plt.xlabel('X Value')
plt.ylabel('Y Value')

print 'Correlation: ' + str(np.cov(X,Y)[0,1]/(np.std(X)*np.std(Y)))

print 'Built-in correlation: ' + str(np.corrcoef(X,Y)[0,1])

''' correlation p-value - whether or not two things are related... but correlation may jnot lend itself to p-values.'''

#deje 15:10

#key is to determine whether correlation is significant
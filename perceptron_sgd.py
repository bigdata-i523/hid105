import numpy as np
from matplotlib import pyplot as plt

def perceptron_sgd(X, Y):
	 w = np.zeros(len(X[0]))
	 eta = 1
	 epochs = 10
	 for i in range(0, epochs):
		 for j in range(0, len(X)):
			 if np.dot(X[j], w) *Y[j] <= 0:
				 w += X[j] * Y[j]
	 return w




X = np.array([
    [-2,4,-1],
    [4,1,-1],
    [1, 6, -1],
    [2, 4, -1],
    [6, 2, -1],
 ])

y = np.array([-1,-1,1,1,1])

perceptron_sgd(X, y)
#output:
#array([ 3.,  4.,  9.])


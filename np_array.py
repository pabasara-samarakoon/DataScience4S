import numpy as np # numpy used for numbers , arrays...
import matplotlib.pyplot as plt # for visualization
np.random.seed(10) #when we set seed , produced result same at all times , without seed it is changed time to time
a = np.array([2,5,8])
print ('a =' , a)
b = np.array([[1,2,3],[8,6,9]])
print ('b =' ,b)
c = np.array([[4,5,6],[7,3,4]])
print ('c =' ,c)
"""a1 = np.array([5,6,7])
print ('a1 =' ,a1)
a2 = np.array([1,2,3])
print ('a2 =' ,a2)
arr = np.append(a1,a2)
print('arr =' ,arr)
print('shape of arr = ' ,arr.shape)
arr2 = np.append(a1,a2, axis=0 )
print('arr2 =' ,arr2)
print('shape of arr2 = ' ,arr2.shape)
print('shape of b', b.shape)
print('shape of c', c.shape)"""
bc = np.append(b,c, axis=0 )
print('shape of bc', bc.shape)
bc2 = np.append(b,c, axis=1 )
print('shape of bc2', bc2.shape)
print('shape of a', a.shape)
a = a.reshape([1,3]) # otherwise we can add two brackets when initializing array [[...]]
print('shape of a', a.shape)
ac = np.append(a,c, axis=1 )
print('shape of ac', ac.shape)


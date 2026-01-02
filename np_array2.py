import numpy as np # numpy used for numbers , arrays...
import matplotlib.pyplot as plt # for visualization
np.random.seed(10) #when we set seed , produced result same at all times , without seed it is changed time to time

N = 200
m = 2
c = 1
mu = 5 
std = 1 

def visualize(x,y):
    plt.scatter(x,y)
    plt.title("Data")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

noise = np.random.randn(N) * 1
x = mu + std*np.random.randn(N) 
x = x.reshape([N,1])  
y = m*x + c + noise

def getX(x):
    b = np.ones([N,1])
    X = np.append(x,b, axis=1)
    return X

#print('x' ,x.shape)
X = getX(x) #data matrix
print('X ',X.shape)
print('y ',y.shape)
#visualize(x,y)
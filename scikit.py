import numpy as np # numpy used for numbers , arrays...
import matplotlib.pyplot as plt # for visualization
from sklearn import linear_model
np.random.seed(10) #when we set seed , produced result same at all times , without seed it is changed time to time

N = 200
m = 2
c = 1
mu = 5 

std = 1 

def visualize(x,y,yh):
    plt.plot(x,y,'b.')#blue for test data
    plt.plot(x,yh,'r.')#red for 
    plt.title("Data")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def getX(x):
    b = np.ones([N,1])
    X = np.append(x,b, axis=1)
    return X

#z = np.linalg.inv(np.dot(np.dot(np.dot(X.T,X)),X.T),y)
def calTheta(X,y):
    XT = X.T
    theta = np.linalg.inv(np.dot(XT,X))
    theta = np.dot(theta,XT)
    theta = np.dot(theta,y)
    return theta

def calPrediction(theta,X):
    return np.dot(X,theta)

noise = np.random.randn(N,1) * 1
x = mu + std*np.random.randn(N,1)   
y = m*x + c + noise

X = getX(x) 
theta = calTheta(X,y)
print(theta)
reg = linear_model.LinearRegression().fit(x,y)
print(reg.coef_)
print(reg.intercept_)






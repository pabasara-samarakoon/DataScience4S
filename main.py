import numpy as np # numpy used for numbers , arrays...
import matplotlib.pyplot as plt # for visualization
np.random.seed(10) #when we set seed , produced result same at all times , without seed it is changed time to time
##----------generate random numbers----------
#x = np.random.randn(5)
##------------print random numbers-------------
#print(x)
##---------print mean of x -----------------for larger no of numbers , mean of x become closed to 0 
#print(np.mean(x))
##------generate random matrix----------
#x = np.random.randn(5,2) -----------for randn it is normal distribution
#x = np.random.rand(5,2) ------------ for rand it is uniform distribution
##-------print matrix------------
#print(x)


####################
N = 200
m = 2
c = 1
mu = 5 #for shift from 0 ,
std = 1 #for change scale 
noise = np.random.randn(N) * 0.2 # generate noise , here * 0.2 used to increase space of dots
#fumnction for visualize
def visualize(x,y):
    plt.scatter(x,y)
    plt.title("Data")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
#x = np.random.rand(N)
x = mu + std*np.random.rand(N)   
#y = m*x + c  -- no noise
y = m*x + c + noise
#print(y)
visualize(x,y)
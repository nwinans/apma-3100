import numpy as np 
import matplotlib.pyplot as plt
import math

tau = 57
a = 1 / tau
x = np.linspace(0, 100, 1000)

def f_X (x):
    return a*a*x*math.exp(-a*a*x*x/2)

fX = np.vectorize(f_X)
plt.plot(x, fX)
plt.show()
import numpy as np 
import matplotlib.pyplot as plt
import math

tau = 57
a = 1 / tau
x = np.linspace(0, 200, 500)

def f_X (x):
    return a*a*x*math.exp(-a*a*x*x/2)

def F_X (x):
    return 1 - math.exp(-a*a*x*x/2)

fX = np.vectorize(f_X)
FX = np.vectorize(F_X)

plt.plot(x, fX(x))
plt.plot(x, FX(x))
plt.show()
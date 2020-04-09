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

def x_from_p (p):
    return math.sqrt(-2*math.log(1-p)/(a*a))

circle50 = plt.Circle((0, 0) x_from_p(.5))
circle70 = plt.Circle((0, 0) x_from_p(.7))
circle90 = plt.Circle((0, 0) x_from_p(.9))


print(x_from_p(.5))
print(x_from_p(.7))
print(x_from_p(.9))
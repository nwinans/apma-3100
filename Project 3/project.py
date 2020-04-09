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
plt.savefig("pdf_and_cdf_3.png")

circle50 = plt.Circle((0, 0), x_from_p(.5), facecolor='None', edgecolor='r', zorder=1)
circle70 = plt.Circle((0, 0), x_from_p(.7), facecolor='None', edgecolor='b', zorder=2)
circle90 = plt.Circle((0, 0), x_from_p(.9), facecolor='None', edgecolor='g', zorder=3)

plt.cla()
plt.gca().axis('equal')
plt.gca().set_xlim((-200, 200))
plt.gca().set_ylim((-200, 200))

plt.gca().add_artist(circle50)
plt.gca().add_artist(circle70)
plt.gca().add_artist(circle90)

plt.savefig('circles_3.png')

def mean(realizations):
    sum = 0
    for i in range(realizations):
        sum += x_from_p(i)
    return sum/realizations

def x_i(i):
    if(i == 0):
        return 1000
    return (24693*x_i(i-1)+3967)%(2**17)

def u_i(i):
    return x_i(i)/(2**17)

def x_from_p (p):
    return math.sqrt(-2*math.log(1-p)/(a*a))

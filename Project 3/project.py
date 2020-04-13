import numpy as np 
import matplotlib.pyplot as plt
import math
import sys
sys.setrecursionlimit(1000000000)

tau = 57
a = 1 / tau
x = np.linspace(0, 200, 500)

def f_X (x):
    return a*a*x*math.exp(-a*a*x*x/2)

def F_X (x):
    return 1 - math.exp(-a*a*x*x/2)

def x_from_p(p):
    return math.sqrt(-2*math.log(1-p)/(a*a))

fX = np.vectorize(f_X)
FX = np.vectorize(F_X)

plt.plot(x, fX(x))
plt.plot(x, FX(x))
plt.savefig("pdf_and_cdf_3.png")

def x_from_p (p):
    return math.sqrt(-2*math.log(1-p)/(a*a))

prev_x = -1

def x_i():
    global prev_x
    if(prev_x == -1):
        prev_x = 1000
        return prev_x
    prev_x = (24693*prev_x+3967)%(2**17)
    return prev_x

def u_i():
    return x_i()/(2**17)

def M_n(n,start):
    sum = 0
    for i in range(start, start+n):
        u = u_i()
        s = x_from_p(u)
        sum += s
    return sum/n

start = 0

def realizations(sample):
    global start
    ret = []
    for i in range(110):
        ret.append(M_n(sample,start))
        start += sample
    return ret

m_10 = realizations(10)
m_30 = realizations(30)
m_50 = realizations(50)
m_100 = realizations(100)
m_150 = realizations(150)
m_250 = realizations(250)
m_500 = realizations(500)
m_1000 = realizations(1000)
x_n = [10 for i in range(110)] + [30 for i in range(110)] + [50 for i in range(110)] + [100 for i in range(110)] + [150 for i in range(110)] + [250 for i in range(110)] + [500 for i in range(110)] + [1000 for i in range(110)]
y_n = m_10 + m_30 + m_50 + m_100 + m_150 + m_250 + m_500 + m_1000

plt.cla()
plt.scatter(x_n, y_n)
plt.savefig("realizations.png")

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
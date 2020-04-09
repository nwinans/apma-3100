from math import log as ln
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.setrecursionlimit(10000)

dial_time = 6
busy_signal_time = 3
not_there_time = 25
hang_up_time = 1
average_ring_time = 12
realizations = 1000
r_var = 1
totalTime = 0
time_list = []
cdf_pts = [(6, 0)]

def x_i(i):
    if(i == 0):
        return 1000
    return (24693*x_i(i-1)+3517)%(2**15)

def u_i(i):
    return x_i(i)/(2**15)

# return value is a tuple where the first value is if someone picked up and the second value is the ring time 
def ring_time(r_num):
    ring_time = dial_time # always have to dial 
    
    if r_num <= 0.2: # probability that line is busy is 0.2
        ring_time += busy_signal_time
    elif r_num <= 0.5: # probability that no is available to answer is 0.3 -> 0.2 + 0.3 = 0.5 
        ring_time += not_there_time
    else: # someone is available to answer
        r_num = (r_num - 0.5) * 2 # recalibrate variable, but keep it between 0 and 1
        if r_num >= (1-0.1245): # someone is available but they didn't pick up
            ring_time += not_there_time # time for rings
        else:
            return (True, ring_time - (average_ring_time * ln(1 - r_num))) # exponential probability (P = 1 - exp(-lambda*t)) solved for t, added to the ring_time

    ring_time += 1 # hang up time
    return (False, ring_time) # no one picked up, return that and the ring time

def call():
    total_time = 0
    global r_var, totalTime, time_list
    for _ in range (0, 4):
        c = ring_time(u_i(r_var))
        r_var += 1
        total_time += c[1]
        if c[0] is True:
            break
    time_list.append(total_time)
    totalTime += total_time

    return total_time

for _ in range(0, realizations):
    call()

time_list = sorted(time_list)

print("Mean: " + str(totalTime/realizations))
print("First Quartile: " + str(time_list[int((realizations/4) - 1)]))
print("Median: " + str(time_list[int((realizations/2) - 1)]))
print("Third Quartile: " + str(time_list[int((3*realizations/4) - 1)]))

for i in range(0, realizations):
    if time_list[i] > 15:
        print("P[W<=15]: " + str(i/realizations))
        cdf_pts.append((15, i/realizations))
        break

for i in range(0, realizations):
    if time_list[i] > 20:
        print("P[W<=20]: " + str(i/realizations))
        cdf_pts.append((20, i/realizations))
        break

for i in range(0, realizations):
    if time_list[i] > 30:
        print("P[W<=30]: " + str(i/realizations))
        cdf_pts.append((30, i/realizations))
        break

for i in range(0, realizations):
    if time_list[i] <= 40:
        continue
    print("P[W>40]: " + str(1 - i/realizations))
    cdf_pts.append((40, i/realizations))
    break

for i in range(0, realizations):
    if time_list[i] <= 60:
        continue
    print("P[W>60]: " + str(1 - i/realizations))
    cdf_pts.append((60, i/realizations))
    break

for i in range(0, realizations):
    if time_list[i] <= 75:
        continue
    print("P[W>75]: " + str(1 - i/realizations))
    cdf_pts.append((75, i/realizations))
    break

for i in range(0, realizations):
    if time_list[i] <= 100:
        continue
    print("P[W>100]: " + str(1 - i/realizations))
    cdf_pts.append((100, i/realizations))
    break

cdf_pts.append((128, 1))
data_in_array = np.array(cdf_pts)
tranposed = data_in_array.T
x, y = tranposed
plt.plot(x, y)
plt.ylabel("Cumulative Probability")
plt.xlabel("W")
plt.title("CDF of W")
plt.show()
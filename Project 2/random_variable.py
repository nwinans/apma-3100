from math import log as ln
import sys

sys.setrecursionlimit(10000)

dial_time = 7.626
busy_signal_time = 4.365
not_there_time = 35.4
hang_up_time = 1.32
average_ring_time = 15.15
realizations = 1000
r_var = 1
totalTime = 0
time_list = []

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
    for i in range (0, 4):
        c = ring_time(u_i(r_var))
        r_var += 1
        total_time += c[1]
        if c[0] is True:
            break
    time_list.append(total_time)
    totalTime += total_time

    return total_time

for _ in range(0, 1000):
    call()

time_list = sorted(time_list)

print("Mean: " + str(totalTime/1000))
print("First Quartile: " + str(time_list[249]))
print("Median: " + str(time_list[499]))
print("Third Quartile: " + str(time_list[749]))
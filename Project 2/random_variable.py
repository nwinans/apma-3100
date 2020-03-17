from math import log as ln

dial_time = 6
busy_signal_time = 3
not_there_time = 25

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
            ring_time += 25 # time for rings
        else:
            return (True, ring_time - 12 * ln(1 - r_num)) # exponential probability (P = 1 - exp(-lambda*t)) solved for t, added to the ring_time

    ring_time += 1 # hang up time
    return (False, ring_time) # no one picked up, return that and the ring time

#tests
print(ring_time(.99)) # no one answers
print(ring_time(.8)) # someone answers
print(ring_time(.93775)) # 5 rings
print(ring_time(.93774)) # just less than 5 rings
print(ring_time(.5)) # no one is available to answer
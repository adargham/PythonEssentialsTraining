#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# simple fibonacci series
# the sum of two elements defines the next set

import matplotlib.pyplot as pp

N = int(input("Number of elements in Fibonacci Series: "))
f =[0, 1]

if N > 2:
    for i in range (2, N+1):
        nextElement = f[i-1]+ f[i-2]
        f.append(nextElement)

x = list(range(N+1))


print(x)
print(f)

pp.plot(x,f)
pp.show()






#!/usr/bin/python

import math

N = 100000
outputMod = 100

t0 = 0
t1 = 8*math.pi
dx = (t1-t0)/float(N)

def funkcia(x):
    if (x==0):
        return 1
    return math.sin(x)/x;

f = open('sincintegral.dat', 'w')
suma = 0;
for i in range(N+1):
    x = (float(i)/N * (t1-t0) +t0)
    y = funkcia(x);
    suma += y*dx;
    if (i % outputMod == 0):
        f.write("%.6f %.6f %.6f\n" %(x, y, suma))


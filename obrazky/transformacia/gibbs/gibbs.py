#!/usr/bin/python

import math

N = 1000

def linear(x):
    return 0.5*(math.pi-x)

def saw(x):
    if (x>math.pi):
        return 1
    return 0
    
def linearSeries(n,x):
    s = 0
    for k in range(1,n+1):
        s += math.sin(k*x)/k
    return s

def sawSeries(n,x):
    s = 0.5
    for k in range(1,n+1):
        s += 2.0/math.pi *math.sin((2*k-1)*x)/(2*k-1)
    return s

def linearSeries10(x):
    return linearSeries(10,x)

def linearSeries100(x):
    return linearSeries(100,x)

def linearSeries1000(x):
    return linearSeries(1000,x)

def sawSeries100(x):
    return sawSeries(100,x)

def sawSeries10(x):
    return sawSeries(10,x)

def writeFile(filename, funkcia, suma, t0, t1):
    f = open(filename, 'w')
    for i in range(N+1):
        x=(float(i)/N * (t1-t0) +t0)*math.pi
        f.write("%.6f %.6f %.6f\n" %(x, 
            funkcia(x), suma(x)))

writeFile('lin_10.dat', linear, linearSeries10,0,1);
writeFile('lin_100.dat', linear, linearSeries100,0,1);
writeFile('lin_1000.dat', linear, linearSeries1000,0,1);
writeFile('lin_1000_2.dat', linear, linearSeries1000,0,0.1);
writeFile('saw_100.dat', saw, sawSeries100,-1,1);
writeFile('saw_10.dat', saw, sawSeries10,-1,1);

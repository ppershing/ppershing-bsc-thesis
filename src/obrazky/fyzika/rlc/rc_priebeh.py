#!/usr/bin/python

import math

N = 1000


def sum(N,funkcia):
    sum = 0
    for i in range(N):
        sum+= funkcia(i)
    return sum

def save(f, funkcia):
    t0 = -math.pi
    t1 = math.pi
    for i in range(N+1):
        x = (float(i)/N * (t1-t0) +t0)
        y = funkcia(x);
        f.write("%.6f %.6f\n" %(x, y))

def clen(w, rc,t):
    if w==0:
        return 0.5
    if w%2 == 0:
        return 0
    return 2/math.pi/w * (math.sin(w*t) - w*rc*math.cos(w*t))/(1+w*w*rc*rc)

save(open('rc_priebeh_01.dat', 'w'), 
        lambda t:sum(100, lambda x,y=t: clen(x, 0.1, y)))

save(open('rc_priebeh_05.dat', 'w'), 
        lambda t:sum(100, lambda x,y=t: clen(x, 0.5, y)))

save(open('rc_priebeh_10.dat', 'w'), 
        lambda t:sum(100, lambda x,y=t: clen(x, 1.0, y)))

save(open('rc_priebeh_20.dat', 'w'), 
        lambda t:sum(100, lambda x,y=t: clen(x, 2.0, y)))

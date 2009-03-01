#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 10cm,4cm 
set output "example_pulse.eps"

set samples 1000

set xrange[-pi:pi]

f(x) = (x<0) ? 0: 1
F(m,x) = (m==0)?0.5: 2/pi * sin((2*m-1)*x) / (2*m-1)
S(n,x) = (n < 0) ? 0: F(n,x) + S(n-1,x)

plot f(x), \
    S(0,x), \
    S(1,x), \
    S(2,x), \
    S(3,x)

#pause -1

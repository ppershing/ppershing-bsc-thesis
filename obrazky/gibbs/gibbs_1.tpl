#!/usr/bin/gnuplot.exe

#set terminal postscript eps color size 10cm,4cm 
#set output "example_saw.eps"

set samples 1000

set xrange[0:pi]
set yrange[0:2]
f(x) = 1/2.0*(pi-x)
F(m,x) = (m==0)? 0 : sin(m*x)/m
S(n,x) = (n < 0) ? 0: F(n,x) + S(n-1,x)

plot f(x), \
    S(10,x), \
    S(50,x), \
    S(99,x)

pause -1

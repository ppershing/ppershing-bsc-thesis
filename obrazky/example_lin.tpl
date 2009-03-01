#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 10cm,4cm 
set output "example_lin.eps"

set samples 1000

set xrange[-pi:pi]

g(x) = cos(x*pi)
f(x) = x
F(m,x) = (m==0)? 0 : 2 * g(m+1)/m*sin(m*x)
S(n,x) = (n < 0) ? 0: F(n,x) + S(n-1,x)

plot f(x), \
    S(1,x), \
    S(2,x), \
    S(3,x)

#pause -1

#!/usr/bin/gnuplot.exe

#set terminal postscript eps color size 7cm,4cm 
#set output "ideal_highpass.eps"

set xrange[-15:15]

set samples 31

bin(n,p) = exp( lgamma(n+1) - lgamma(p+1) - lgamma(n-p+1))
binomial(n,p) = bin(n, floor(p+0.001)) / 2**n

plot binomial(15,7+x) with points

pause -1

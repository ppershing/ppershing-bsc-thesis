#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 7cm,4cm 
set output "iterated_median.eps"

set xrange[-7:7]

set samples 15
set yrange[0:0.6]

bin(n,p) = p>=0? n>=p?exp( lgamma(n+1) - lgamma(p+1) -lgamma(n-p+1)):0:0
binomial(n,p) = bin(n, floor(n/2) + floor(p+0.001)) / 2**n

set pointsize 2
plot binomial(2,x) with points,\
     binomial(4,x) with points,\
     binomial(8,x) with points,\
     binomial(16,x) with points,\
     binomial(30,x) with points
    

#pause -1

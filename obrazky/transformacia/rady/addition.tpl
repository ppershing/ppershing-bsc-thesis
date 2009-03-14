#!/usr/bin/gnuplot.exe
set terminal postscript eps color size 5cm,3cm 
set output "addition.eps"
set xrange[-3:3]
set samples 1000
plot sin(pi*x),-0.7*sin(2*pi*x), sin(pi*x)-0.7*sin(2*pi*x) \
    with lines lw 2 lt 2

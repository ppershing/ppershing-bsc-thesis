#!/usr/bin/gnuplot.exe
set terminal postscript eps color size 5cm,3cm 
set output "frequency_difference.eps"
set xrange[-1:1]
set samples 5000
plot sin(pi*x),sin(2*pi*x), sin(3*pi*x)

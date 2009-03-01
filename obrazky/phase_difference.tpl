#!/usr/bin/gnuplot.exe
set terminal postscript eps color size 5cm,3cm 
set output "phase_difference.eps"
set xrange[-1:1]
set samples 5000
plot sin(pi*x),sin(pi*x+pi/2)

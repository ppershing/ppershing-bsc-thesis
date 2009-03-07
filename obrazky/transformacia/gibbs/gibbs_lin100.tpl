#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 10cm,4cm 
set output "gibbs_lin100.eps"

set xrange[0:pi]
set yrange[0:2]

plot 'lin_100.dat' using 1:3 with lines

#pause -1

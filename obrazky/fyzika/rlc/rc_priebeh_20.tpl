#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 7cm,4cm 
set output "rc_priebeh_20.eps"

set xrange[-pi:pi]
set yrange[0:1]

plot 'rc_priebeh_20.dat' using 1:2 with lines, \
     (x<0)?exp(-(x+pi)/2.0): 1-exp(-x/2.0) with lines

#pause -1

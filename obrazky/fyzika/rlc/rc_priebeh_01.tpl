#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 7cm,4cm 
set output "rc_priebeh_01.eps"

set xrange[-pi:pi]
set yrange[0:1]

plot 'rc_priebeh_01.dat' using 1:2 with lines, \
     (x<0)?exp(-(x+pi)/0.1): 1-exp(-x/0.1) with lines

#pause -1

#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 10cm,4cm 
set output "gibbs_lin1000_2.eps"

set xrange[0:0.1]
set yrange[1.4:1.85]

plot 'lin_1000_2.dat' using 1:2 with lines, \
    'lin_1000_2.dat' using 1:3 with lines

#pause -1

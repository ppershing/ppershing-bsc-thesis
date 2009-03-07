#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 10cm,4cm 
set output "gibbs_saw10.eps"

set xrange[-pi:pi]
set yrange[-0.2:1.2]

plot 'saw_10.dat' using 1:3 with lines

#pause -1

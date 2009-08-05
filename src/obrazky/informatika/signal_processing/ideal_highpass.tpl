#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 7cm,4cm 
set output "ideal_highpass.eps"

set xrange[0:1]
set yrange[0:1.5]

plot (x>0.7)?1:0 with lines;

#pause -1

#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 7cm,4cm 
set output "ideal_highpass_3d.eps"

set xrange[-1:1]
set yrange[-1:1]
set zrange[0:1]

set isosamples 30

splot (sqrt(x**2 + y**2)>0.7)?1:0 with lines;

#pause -1

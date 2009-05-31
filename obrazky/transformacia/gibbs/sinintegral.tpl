#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 10cm,4cm 
set output "sinintegral.eps"

#set xrange[-pi:pi]
#set yrange[-0.2:1.2]

plot 'sinintegral.dat' using 1:3 with lines

#pause -1

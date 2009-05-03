#!/usr/bin/gnuplot.exe


set terminal postscript eps color size 7cm,4cm
set output "sine_window.eps"


n=128

set xrange[0:n-1]
set samples n
plot sin( pi/n * (x+0.5)) with points

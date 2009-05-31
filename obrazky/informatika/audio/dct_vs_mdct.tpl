#!/usr/bin/gnuplot.exe

set terminal postscript eps color size 7cm,4cm
set output "dct_vs_mdct.eps"

set xrange[120:140]
set yrange[0.2:0.5]

plot 'sample.dat' with points,\
    'dct.dat' with points, \
    'mdct.dat' with points


set parametric
set trange[-0.5:0.5]
replot 127.5,t

#pause -1

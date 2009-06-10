#!/usr/bin/gnuplot.exe

set terminal postscript eps enhanced size 9cm,6cm
set output "dct_vs_mdct.eps"
set multiplot 

set xrange[112:144]
set yrange[0.2:0.6]

set xtics 8
plot 'sample.dat' title "Zvuk" with points pt 1,\
    'dct.dat' title "DCT" with points pt 3, \
    'mdct.dat' title "MCDT" with points pt 4


set parametric
set trange[0.2:0.6]
set key bottom
plot 127.75,t title "Hranica okna" with lines lt 4

#pause -1

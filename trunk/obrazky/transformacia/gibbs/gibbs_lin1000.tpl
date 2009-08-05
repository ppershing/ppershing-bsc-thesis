#!/usr/bin/gnuplot.exe

load "gibbs_template.tpl"
set output "gibbs_lin1000.eps"

set xrange[0:pi]
set yrange[0:2]

plot 'lin_1000.dat' using 1:3 title "S_{1000}(x)" with lines ls 2

#pause -1

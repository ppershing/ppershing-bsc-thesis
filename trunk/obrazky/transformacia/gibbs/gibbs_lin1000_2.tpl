#!/usr/bin/gnuplot.exe

load "gibbs_template.tpl"
set output "gibbs_lin1000_2.eps"

set xrange[0:0.1]
set yrange[1.4:1.85]

plot 'lin_1000_2.dat' using 1:2 title "f(x)" with lines ls 1, \
     'lin_1000_2.dat' using 1:3 title "S_{1000}(x)" with lines ls 2

#pause -1

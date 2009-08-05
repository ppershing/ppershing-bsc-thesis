#!/usr/bin/gnuplot.exe

load "gibbs_template.tpl"
set output "gibbs_lin10.eps"

set xrange[0:pi]
set yrange[0:2]

plot 'lin_10.dat' using 1:2 title "f(x)"  with lines ls 1,\
     'lin_10.dat' using 1:3 title "S_{10}(x)" with lines ls 2

#pause -1

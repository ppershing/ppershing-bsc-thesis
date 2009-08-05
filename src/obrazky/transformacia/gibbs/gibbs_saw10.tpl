#!/usr/bin/gnuplot.exe

load "gibbs_template.tpl"
set output "gibbs_saw10.eps"

set xrange[-pi:pi]
set yrange[-0.2:1.2]

f(x) = (x<0)?0:1
set key left
plot f(x) title "f(x)" with lines ls 1,\
     'saw_10.dat' using 1:3 title "S_{10}(x)" with lines ls 2

#pause -1

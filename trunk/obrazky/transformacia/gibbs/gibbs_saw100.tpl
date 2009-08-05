#!/usr/bin/gnuplot.exe

load "gibbs_template.tpl"
set output "gibbs_saw100.eps"

set xrange[-pi:pi]
set yrange[-0.2:1.2]

set key left
plot 'saw_100.dat' using 1:3 title "S_{100}(x)" with lines ls 2

#pause -1

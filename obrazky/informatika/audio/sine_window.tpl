#!/usr/bin/gnuplot.exe


set terminal postscript eps enhanced size 7cm,5cm
set output "sine_window.eps"


n=128

set key bottom left
set xtics 16
set xrange[0:n-1]
set samples n
plot sin( pi/n * (x+0.5)) title "sin {/Symbol p}/128(x+0.5)" with points ps 1

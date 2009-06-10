#!/usr/bin/gnuplot.exe
set terminal postscript eps enhanced size 5cm,4cm 
set output "frequency_difference.eps"
set xrange[-1:1]
set samples 5000
set key below
plot sin(pi*x) title "sin {/Symbol p}x" ls 1,\
     sin(2*pi*x) title "sin 2{/Symbol p}x" ls 2,\
     sin(3*pi*x) title "&{dummy}sin 3{/Symbol p}x" ls 4

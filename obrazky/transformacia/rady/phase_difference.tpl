#!/usr/bin/gnuplot.exe
set terminal postscript eps enhanced size 5cm,4cm 
set output "phase_difference.eps"
set key below
set xrange[-1:1]
set samples 5000

plot sin(pi*x) title "sin {/Symbol p}x" ls 1,\
     sin(pi*x+pi/4) title "sin ({/Symbol p}x + {/Symbol p}/4)" ls 2,\
     sin(pi*x+pi/2) title "sin ({/Symbol p}x + {/Symbol p}/2)" ls 4

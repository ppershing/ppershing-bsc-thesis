#!/usr/bin/gnuplot.exe
set terminal postscript eps enhanced size 5cm,4cm
set output "addition.eps"
set xrange[-3:3]
set samples 1000
set key below
plot sin(pi*x) title "sin {/Symbol p}x" \
        with lines ls 1,\
    -0.7*sin(2*pi*x) title "-0.7sin 2{/Symbol p}x" \
        with lines ls 2,\
    sin(pi*x)-0.7*sin(2*pi*x) \
        title "sin {/Symbol p}x - 0.7sin 2{/Symbol p}x" \
        with lines ls 4

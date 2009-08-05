#!/usr/bin/gnuplot.exe

set terminal postscript eps enhanced size 10cm,5cm 
set output "sincintegral.eps"

#set xrange[-pi:pi]
#set yrange[-0.2:1.2]

set xtics ("{/Symbol p}" pi, "2{/Symbol p}" 2*pi, \
           "3{/Symbol p}" 3*pi, "4{/Symbol p}" 4*pi, \
           "5{/Symbol p}" 5*pi, "6{/Symbol p}" 6*pi, \
           "7{/Symbol p}" 7*pi, "8{/Symbol p}" 8*pi)

set key spacing 2.0
plot 'sincintegral.dat' using 1:3 \
    title "{/Symbol=18 \362}@_0^x sinc t {/Helvetica d}t&{xx}" with lines ls 1

#pause -1

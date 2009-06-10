#!/usr/bin/gnuplot.exe

set terminal postscript eps enhanced size 17cm,10cm 
set output "dirichlet_kernel.eps"

set samples 1000
D(x,n,L) = sin((2*n+1)*pi*x / (2 * L)) / sin(pi*x/(2*L))


set xrange[-3:3]
set yrange[-20:80]

set multiplot

set pointsize 2
set origin 0,0.5
set size 0.45,0.45
set title "n=10"
plot D(x,10,pi) title "D_{10}(x)"

set origin 0.5,0.5
set title "n=20"
plot D(x,20,pi) title "D_{20}(x)"

set origin 0,0
set title "n=30"
plot D(x,30,pi) title "D_{30}(x)"

set origin 0.5,0
set title "n=40"
plot D(x,40,pi) title "D_{40}(x)"

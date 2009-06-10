#!/usr/bin/gnuplot.exe

load "example_template.tpl"
set output "example_lin.eps"

g(x) = cos(x*pi)
f(x) = x
F(m,x) = (m==0)? 0 : 2 * g(m+1)/m*sin(m*x)
S(n,x) = (n < 0) ? 0: F(n,x) + S(n-1,x)

set key left
plot f(x) title "f(x)" ls 1, \
    S(2,x) title "S_2(x)" ls 2, \
    S(8,x) title "S_8(x)" ls 3, \
    S(32,x) title "S_32(x)" ls 5

#pause -1

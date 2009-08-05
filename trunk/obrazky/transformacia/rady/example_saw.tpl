#!/usr/bin/gnuplot.exe

load "example_template.tpl"
set output "example_saw.eps"

g(x) = cos(x*pi)
f(x) = abs(x)
F(m,x) = (m==0)? 0.5*pi : -4/pi*cos((2*m-1)*x)/(2*m-1)**2 
S(n,x) = (n < 0) ? 0: F(n,x) + S(n-1,x)

plot f(x) title "f(x)" ls 1, \
    S(1,x) title "S_1(x)" ls 2, \
    S(2,x) title "S_2(x)" ls 3, \
    S(3,x) title "S_3(x)" ls 5

#pause -1

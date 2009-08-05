#!/usr/bin/gnuplot.exe

load "example_template.tpl"
set output "example_pulse.eps"

f(x) = (x<0) ? 0: 1
F(m,x) = (m==0)?0.5: 2/pi * sin((2*m-1)*x) / (2*m-1)
S(n,x) = (n < 0) ? 0: F(n,x) + S(n-1,x)

set key left

plot f(x) title "f(x)" ls 1, \
    S(1,x) title "S_1(x)" ls 2, \
    S(2,x) title "S_2(x)" ls 3, \
    S(4,x) title "S_4(x)" ls 4, \
    S(8,x) title "S_8(x)" ls 5

#pause -1

import cmath
import math


def Integrate(f,t_0,t_1,n):
    sum = 0
    dx = (t_1 - t_0)/float(n);
    for i in range(n):
        x = dx * i + t_0
        sum += f(x)
    return sum * dx

def FractionalExp(fi,t,w):
#    return cmath.exp(2j * math.pi * \
#        (-w * t + 0.5 * t ** 2 * math.cos(fi))\
#        / math.sin(fi))
     return cmath.exp(1j * \
        (math.cos(fi) * 0.5 * t**2 - w*t)/math.sin(fi))

def FractionalFourierTransform(a,f,w):
    if (a==0):
        return complex(f(w))

    fi = 0.5 * math.pi * a
    norm = cmath.exp(-1j * (0.25 * math.pi - 0.5 * fi))
    norm /= (2 * math.pi * math.sin(fi))**0.5
    norm *= cmath.exp(0.5j * math.cos(fi)/math.sin(fi) * w * w)
    integral = Integrate(lambda t: f(t) * FractionalExp(fi,t,w),
            -math.pi, math.pi, 20000)
    return integral * norm

def rect(x):
    if (abs(x)<math.pi):
        return 1 
    return 0

def SaveFractionalTransform(filename, funct, t_0, t_1, n, a):
    print "save", filename
    f = open(filename+'.dat', 'w')

    dx = (t_1 - t_0)/float(n);
    for i in range(n):
        x = dx * i + t_0
        y = FractionalFourierTransform(a, funct, x)
        f.write("%.7f %.7f %.7f\n" % (x, y.real, y.imag))

    f.close()
    f = open(filename+'.tpl', 'w')
    f.write('#!/usr/bin/gnuplot.exe\n');
    f.write('set terminal postscript eps color size 5cm, 3cm\n');
    f.write('set output \'%s.eps\'\n' % filename);
    f.write('set xrange[-6:6]\n');
    f.write('set yrange[-1:2.5]\n');
    f.write('plot \'%s.dat\' using 1:2 with lines, \\\n' % filename);
    f.write('     \'%s.dat\' using 1:3 with lines\n' % filename);


SaveFractionalTransform('rect_000', rect, -2*math.pi, 2*math.pi, 100, 0)
SaveFractionalTransform('rect_001', rect, -2*math.pi, 2*math.pi, 100, 0.01)
SaveFractionalTransform('rect_005', rect, -2*math.pi, 2*math.pi, 100, 0.05)
SaveFractionalTransform('rect_020', rect, -2*math.pi, 2*math.pi, 100, 0.20)
SaveFractionalTransform('rect_035', rect, -2*math.pi, 2*math.pi, 100, 0.35)
SaveFractionalTransform('rect_050', rect, -2*math.pi, 2*math.pi, 100, 0.5)
SaveFractionalTransform('rect_065', rect, -2*math.pi, 2*math.pi, 100, 0.65)
SaveFractionalTransform('rect_080', rect, -2*math.pi, 2*math.pi, 100, 0.80)
SaveFractionalTransform('rect_095', rect, -2*math.pi, 2*math.pi, 100, 0.95)
SaveFractionalTransform('rect_099', rect, -2*math.pi, 2*math.pi, 100, 0.99)
SaveFractionalTransform('rect_100', rect, -2*math.pi, 2*math.pi, 100, 1.0)

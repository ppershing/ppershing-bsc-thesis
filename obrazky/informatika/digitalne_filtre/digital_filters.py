from pnm import PNM
from bitutils import BitUtils
from fft2d import FFT2D
from util import *
import util
import colorschemes
import math
from dif import DIF
from filter import *


def SaveFilterResponse(filename, filter):
    size = 128
    data = [ 0.0 for x in range(size) ]
    data[size/2] = 1.0
    DIF.transformInPlace(data)
    data = util._rotate(data)
    for i in range(size):
        data[i] *= filter.response(abs(i - size/2+1))
    data = util._unrotate(data)
    data = [ complex(x).conjugate()/size for x in data]
    DIF.transformInPlace(data)

    f = open(filename, 'w')
    for x in data:
        f.write("%.7f\n" % (x.real,))
    f.close()

def SaveFrequencyResponse(filename, filter):
    size = 64 # half of filter response
    f = open(filename, 'w')
    for i in range(size):
        f.write("%.7f\n" % (filter.response(i),))
    f.close()

def SaveFilteredImage(filename, data, filter):
    tmp = util.dftRotateFromOutput(data)
    h, w = Util.getDimensions(data)
    for i in range(h):
        for j in range(w):
            tmp[i][j] *= filter.response(
                    (abs(i-h/2+1)**2 + abs(j-w/2+1)**2) **0.5)

    tmp = util.dftRotateForOutput(tmp)
    tmp = [[complex(x).conjugate()/w/h for x in row] for row in tmp]
    FFT2D.transform2d(tmp)
    tmp = [[x.real for x in row] for row in tmp]
    PNM.saveColor(filename, tmp, colorschemes.Gray)

def SavePlotfile(filename):
    f = open(filename+'.tpl', 'w')
    f.write('#!/usr/bin/gnuplot.exe\n')
    f.write('set terminal postscript eps color size 7cm,4cm\n');
    f.write('set output "%s.eps"\n' % filename)
    #f.write('set xrange[0:63]\n')
    f.write('plot \'%s.dat\' with points\n' % filename)
    

def SaveAll(file_prefix, filter, frequency, data):
    print "Saving ", file_prefix
    SaveFilterResponse('%s_response_%d.dat' % (file_prefix, frequency), filter)
    SaveFrequencyResponse('%s_frequency_%d.dat' % (file_prefix, frequency), filter)
    SavePlotfile('%s_response_%d' % (file_prefix, frequency))
    SavePlotfile('%s_frequency_%d' % (file_prefix, frequency))
    SaveFilteredImage('%s_%d.ppm' % (file_prefix, frequency), data, filter)

source_lowpass = PNM.loadToGreyscale('source_lowpass.ppm')
source_highpass = PNM.loadToGreyscale('source_highpass.ppm')
FFT2D.transform2d(source_lowpass)
FFT2D.transform2d(source_highpass)

for freq in [10,20,40]:
    SaveAll('ideal_highpass', IdealHighpass(freq), freq, source_highpass)
    SaveAll('ideal_lowpass', IdealLowpass(freq), freq, source_lowpass)

    SaveAll('gauss_highpass', GaussHighpass(freq), freq, source_highpass)
    SaveAll('gauss_lowpass', GaussLowpass(freq), freq, source_lowpass)
    for order in [1,2,4]:
        SaveAll('butterworth_%d_highpass' % (order,),
        ButterworthHighpass(freq, order), freq, source_highpass)
        SaveAll('butterworth_%d_lowpass' % (order,),
        ButterworthLowpass(freq, order), freq, source_lowpass)

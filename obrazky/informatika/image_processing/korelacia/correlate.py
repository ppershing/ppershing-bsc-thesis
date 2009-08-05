from pnm import PNM
from bitutils import BitUtils
from fft2d import FFT2D
from rectanglestatistics import RectangleStatistics
from util import Util
import colorschemes
import math

def rotatePattern(data):
    tmp = pattern[1:]
    tmp.reverse()
    pattern[1:] = tmp
    for row in pattern:
        tmp = row[1:]
        tmp.reverse()
        row[1:]=tmp 

source = PNM.loadToGreyscale('source.ppm')
pattern = PNM.loadToGreyscale('pattern.ppm')

s_h, s_w = Util.getDimenstions(source)
p_h, p_w = Util.getDimenstions(pattern)

# final width and height for convolution
h = BitUtils.nextPowerOfTwo(s_h + p_h)
w = BitUtils.nextPowerOfTwo(s_w + p_w)

# removing DC offset we achieve better FFT precision
# also, removing is needed for correlation formula
RectangleStatistics.removeDCOffset(pattern)
RectangleStatistics.removeDCOffset(source)
Util.padWithZeros(pattern, w, h)
Util.padWithZeros(source, w, h)
# rotate pattern (transform correlation<->convolution)
rotatePattern(pattern)

print "Fourier size",w,h
print len(pattern), len(pattern[0])
# statistics used to normalize data
source_stats = RectangleStatistics(source)
pattern_sq_sum = sum(map(lambda row: reduce(lambda x,y:x+y**2,row,0) , pattern))

print "Transforming"
FFT2D.transform2d(pattern)
FFT2D.transform2d(source)

print "Convolution"
# we preprocess to use forward transform instead of inverse:
# need to divide by number of points and make complex conjugate
convolution = [[ complex(source[i][j]*pattern[i][j]).conjugate()/w/h \
                 for j in range(w)] for i in range(h)]

print "inverse transform"
FFT2D.transform2d(convolution)

# result array
result = [[0 for j in range(s_w)] for i in range(s_h)]

for i in range(s_h):
    for j in range(s_w):
        # complex part should be zero
        result[i][j] = convolution[i][j].real
        # compute covariance of source square
        sq_avg = source_stats.getSquareAverage(i, j, i + p_h, j + p_w)
        avg = source_stats.getAverage(i, j, i + p_h , j + p_w)
        cov = sq_avg - avg**2
        # normalize result
        result[i][j] /= math.sqrt(cov * p_w * p_h)
        result[i][j] /= math.sqrt(pattern_sq_sum)
        if (result[i][j]<0):
            result[i][j]=0

PNM.saveColor('correlation_color.ppm', result, colorschemes.BlueGreenRed)
PNM.saveColor('correlation_gray.ppm', result, colorschemes.Gray)

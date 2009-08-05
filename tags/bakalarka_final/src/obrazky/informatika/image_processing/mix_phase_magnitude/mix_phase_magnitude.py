from pnm import PNM
from bitutils import BitUtils
from fft2d import FFT2D
from util import Util
import colorschemes
import math

source1 = PNM.loadToGreyscale('source1.ppm')
source2 = PNM.loadToGreyscale('source2.ppm')
#assume that source1/2 have dimensions both powers of two

print "Transforming"
FFT2D.transform2d(source1)
FFT2D.transform2d(source2)

def Mix(source1, source2, MixFunction):
    print "Mixing ..."
    data = [[MixFunction(x, y) for x, y in zip(row1, row2)]
                for row1, row2 in zip(source1, source2)]
    print data[0][0]
    data[0][0] = 0.5 * 512 * 512 # fix brightness offset
    h, w = Util.getDimenstions(data)

    # prepare for inverse transform
    data = [[complex(x).conjugate() / w / h for x in row] for row in data]
    FFT2D.transform2d(data)
    return [[x.real for x in row] for row in data]

PNM.saveColor('p1m1.ppm', Mix(source1, source2, 
        lambda x,y: x), colorschemes.Gray)
PNM.saveColor('p1m2.ppm', Mix(source1, source2, 
        lambda x,y: x/abs(x) * abs(y)), colorschemes.Gray)
PNM.saveColor('p1mc.ppm', Mix(source1, source2, 
        lambda x,y: x/abs(x) * 70), colorschemes.Gray)
PNM.saveColor('p2m1.ppm', Mix(source1, source2, 
        lambda x,y: y/abs(y) * abs(x)), colorschemes.Gray)
PNM.saveColor('p2m2.ppm', Mix(source1, source2, 
        lambda x,y: y), colorschemes.Gray)
PNM.saveColor('p2mc.ppm', Mix(source1, source2, 
        lambda x,y: y/abs(y) * 70), colorschemes.Gray)
PNM.saveColor('pcm1.ppm', Mix(source1, source2, 
        lambda x,y: abs(x)), colorschemes.Gray)
PNM.saveColor('pcm2.ppm', Mix(source1, source2, 
        lambda x,y: abs(y)), colorschemes.Gray)





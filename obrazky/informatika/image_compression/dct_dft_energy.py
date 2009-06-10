from dct_dft import DCT,DFT
from pnm import PNM
import cmath
import math
import colorschemes
from histogram import Histogram

image = PNM.loadToGreyscale('image.ppm')

image = [[ x-0.0 for x in row] for row in image]

dct = DCT.transform2D(image)
dft = DFT.transform2D(image)

def norm(x):
    return math.log(1+abs(x))

koef =1.0/math.log(1+abs(dct[0][0])) # is the same as dft[0][0]

dct_energy = [[math.log(1+abs(x))*koef for x in row] for row in dct]
dft_energy = [[math.log(1+abs(x))*koef for x in row] for row in dft]


k = 200 / 7.0
dct_histogram = Histogram.MakeHistogramImage(\
        reduce(lambda x,y:x+y,dct_energy), 200, 300, k)
dft_histogram = Histogram.MakeHistogramImage(\
        reduce(lambda x,y:x+y,dft_energy), 200, 300, k)

PNM.saveColor('dct_histogram.ppm', dct_histogram, colorschemes.InverseGray)
PNM.saveColor('dft_histogram.ppm', dft_histogram, colorschemes.InverseGray)

PNM.saveColor('dct.ppm', dct_energy, colorschemes.Gray)
PNM.saveColor('dft.ppm', dft_energy, colorschemes.Gray)


import cmath
import math
from bitutils import BitUtils

class DIF:
    def transformInPlace(data):
        n = len(data)
        assert(BitUtils.isPowerOf2(n))


        skip = n

        while skip >= 2:
            for block in range(n/skip):
                for i in range(skip/2):
                    # do butterfly
                    y = data[block * skip + i]
                    z = data[block * skip + skip/2 + i]
                    k = i * (n/skip)
                    twiddle = cmath.exp( -2 * 1j * math.pi / n * k)
                    data[block * skip + i] = y + z
                    data[block * skip + skip/2 +i] = (y - z) * twiddle
            skip /= 2
        BitUtils.bitReverseInPlace(data)


    transformInPlace = staticmethod(transformInPlace)

import math
import cmath

class GeneralTransform:
    def transform2D(cls, data):
        data = apply(zip, [cls.transform(row) for row in data])
        return apply(zip, [cls.transform(row) for row in data])
    transform2D = classmethod(transform2D)
        
class DCT(GeneralTransform):
    def transform(cls, data):
        N = len(data)
        X = []
        for k in range(N):
            s = 0.0
            for n in range(N):
                s += data[n] * math.cos( math.pi / N * (n+0.5)*k)
            X.append(s)
        return X
    transform = classmethod(transform)

class DFT(GeneralTransform):
    def transform(cls, data):
        N = len(data)
        X = []
        for k in range(N):
            s = 0
            for n in range(N):
                s += data[n] * cmath.exp(- 2 * 1j * math.pi/N * k * n)
            X.append(s)
        return X
    transform = classmethod(transform)

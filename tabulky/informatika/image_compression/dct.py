import math
import cmath

class GeneralTransform:
    def transform2D(cls, data):
        data = apply(zip, [cls.transform(row) for row in data])
        return apply(zip, [cls.transform(row) for row in data])
    transform2D = classmethod(transform2D)
    
    def inverseTransform2D(cls, data):
        data = apply(zip, [cls.inverseTransform(row) for row in data])
        return apply(zip, [cls.inverseTransform(row) for row in data])
    inverseTransform2D = classmethod(inverseTransform2D)

    # normalization for jpeg
    def normalize(data):
        assert(len(data)==8)
        assert(len(data[0])==8)
        
        res = [[ x/4.0 for x in row] for row in data]
        for i in range(8):
            res[0][i]/=math.sqrt(2.0)
            res[i][0]/=math.sqrt(2.0)
        return res
    normalize = staticmethod(normalize)
        
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
    
    def inverseTransform(cls, data):
        N = len(data)
        X = []
        for k in range(N):
            s = 0.0
            for n in range(N):
                s += data[n] * math.cos( math.pi / N * (k+0.5)*n)
            X.append(s)
        return X
    inverseTransform = classmethod(inverseTransform)

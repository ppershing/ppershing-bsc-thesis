import math
import cmath

class DCT:
    def transform(data):
        N = len(data)
        X = []
        for k in range(N):
            s = 0.0
            for n in range(N):
                s += data[n] * math.cos( math.pi / N * (n+0.5)*k)
            X.append(s)
        return X
    transform = staticmethod(transform)
    
    def inverseTransform(data):
        N = len(data)
        X = []
        for k in range(N):
            s = data[0]/2.0
            for n in range(1,N):
                s += data[n] * math.cos( math.pi / N * (k+0.5)*n)
            X.append(s*2.0/N)
        return X
    inverseTransform = staticmethod(inverseTransform)

class MDCT:
    def window(data):
        #return data
        N = len(data)
        return [ math.sqrt(2.0) * x * math.sin( math.pi /N * (i+0.5)) for i,x in enumerate(data)]
    window = staticmethod(window)

    def transform(data):
        assert(len(data)%2==0)
        N = len(data)/2
        print N
        result = []
        for k in range(N):
            s = 0.0
            for n in range(2*N):
                s += data[n] * math.cos( math.pi /N * (n + 0.5 + 0.5*N) *
                (k+0.5))
            result.append(s)
        return result
    transform = staticmethod(transform)
        
    def inverseTransform(data):
        N = len(data)
        print N
        result = []
        for k in range(2*N):
            s = 0.0
            for n in range(N):
                s += data[n] * math.cos( math.pi /N * (k + 0.5 + 0.5*N) *
                (n+0.5))
            result.append(s/N)
        return result
    inverseTransform = staticmethod(inverseTransform)

import math;

class Util:
    def padWithZeros(list, w, h):
        for row in list:
            row.extend([ 0.0 for i in range(w-len(row))])
        for i in range(h-len(list)):
            list.append([ 0.0 for i in range(w)])
    padWithZeros = staticmethod(padWithZeros)
            
    def getDimensions(data):
        return len(data), len(data[0])
    getDimensions = staticmethod(getDimensions)

def map2D(function,data):
    res = []
    for row in data:
        res.append(map(function,row))
    return res

def combine2DComplex(abs,arg):
    data = []
    for i in range(len(abs)):
        row = []
        for j in range(len(abs[0])):
            row.append( (math.sin(arg[i][j])*1j +
            math.cos(arg[i][j]))*abs[i][j])
        data.append(row)
    return data


def _rotate(list):
    K = len(list)/2 + 1
    a = list[:K]
    b = list[K:]
    return b+a
    
def _unrotate(list):
    K = len(list) - (len(list)/2 + 1)
    a = list[:K]
    b = list[K:]
    return b+a
    
def sqr(x):
    return x*x

def dftRotateForOutput(data):
    tmp = map(_unrotate, data)
    return _unrotate(tmp)
    
def dftRotateFromOutput(data):
    tmp = map(_rotate, data)
    return _rotate(tmp)

def phase(c):
    return math.atan2(c.imag,c.real)

class MatrixStorage:
    def load(filename):
        f = open(filename, 'r')
        rows = int(f.readline())
        cols = int(f.readline())

        data = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(float(f.readline()))
            data.append(row)
        return data

    load = staticmethod(load)
    
    def save(filename, data):
        f = open(filename, 'w')
        f.write("%d\n%d\n" % (len(data),len(data[0])))

        for row in data:
            for x in row:
                f.write("%f\n" % (x,))
    save = staticmethod(save)

from dif import DIF

class FFT2D:
    def transform2d(data):
        print "Performing 2D transform",len(data),len(data[0])
        for i in range(len(data)):
            DIF.transformInPlace(data[i])
        tmp = list(apply(zip, data))
        print "half done"
        for j in range(len(tmp)):
            tmp[j] = list(tmp[j])
            DIF.transformInPlace(tmp[j])
        tmp2 = list(apply(zip, tmp))
        for i in range(len(tmp2)):
            data[i] = list(tmp2[i])
        print "transform2d done"

    transform2d = staticmethod(transform2d)

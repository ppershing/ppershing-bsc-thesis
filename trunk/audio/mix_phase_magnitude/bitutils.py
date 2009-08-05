class BitUtils:
    def nextPowerOfTwo(x):
        i = 0
        x -= 1 # for power of two, we want same result
        while x > 0:
            i += 1
            x /= 2

        x = 1
        while i > 0:
            i -=1
            x *= 2
        return x
    nextPowerOfTwo = staticmethod(nextPowerOfTwo)

    def isPowerOf2(x):
        return (x & (x - 1)) == 0

    isPowerOf2 = staticmethod(isPowerOf2)

    def log(x):
        i = 0
        x -= 1
        while x > 0:
            i += 1
            x /= 2
        return i        
    log = staticmethod(log)

    def bitReverseInt(x, bits):
        y = 0
        for i in range(bits):
            y = y*2 + x%2
            x /= 2
        return y

    bitReverseInt = staticmethod(bitReverseInt)

    # reverse bits, in place
    def bitReverseInPlace(data):
        n = len(data)
        assert(BitUtils.isPowerOf2(n))
        nlog = BitUtils.log(n)

        for i in range(n):
            j = BitUtils.bitReverseInt(i, nlog)
            if i < j:
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
        return None

    bitReverseInPlace = staticmethod(bitReverseInPlace)


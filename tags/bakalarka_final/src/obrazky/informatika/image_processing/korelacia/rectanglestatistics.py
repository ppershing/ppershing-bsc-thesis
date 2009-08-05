from util import Util

class RectangleStatistics:
    def removeDCOffset(data):
        avg = sum(map(sum, data))
        avg /= reduce(lambda x,y: x*y, Util.getDimenstions(data))
        data[:] = map(lambda x: map(lambda y: y-avg, x), data)
    removeDCOffset = staticmethod(removeDCOffset)

    def __init__(self, data):
        self._h, self._w = Util.getDimenstions(data) 
        self._sum = [[x for x in row ] for row in data]
        self._sq_sum = [[x**2 for x in row ] for row in data]
        self._makeCumulative(self._sum)
        self._makeCumulative(self._sq_sum)

    def _makeCumulative(self, data):
        for i in range(1, self._h):
            data[i][0] += data[i-1][0]
        for j in range(1, self._w):
            data[0][j] += data[0][j-1]
        for i in range(1, self._h):
            for j in range(1, self._w):
                data[i][j] += data[i-1][j] + \
                    data[i][j-1] - data[i-1][j-1]

    def getAverage(self, x1, y1, x2, y2):
        sum = self._getSum(self._sum, x1, y1, x2, y2)
        return sum / (x2 - x1) / (y2 - y1)
    
    def getSquareAverage(self, x1, y1, x2, y2):
        sq_sum = self._getSum(self._sq_sum, x1, y1, x2, y2)
        return sq_sum / (x2 - x1) / (y2 - y1)
 
    def _getSum(self, data, x1, y1, x2, y2):
        if (x2 > self._h) or (y2 > self._w):
            raise Exception("out of bounds")
        x2 -= 1
        y2 -= 1
        x1 -= 1
        y1 -= 1

        tmp = data[x2][y2]
        if (x1 >= 0):
            tmp -= data[x1][y2]
        if (y1 >= 0):
            tmp -= data[x2][y1]
        if (x1 >= 0) and (y1 >=0 ):
            tmp += data[x1][y1]
        return tmp

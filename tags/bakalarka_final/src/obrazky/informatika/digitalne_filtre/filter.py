import math;

#default filter
class Filter:
    def response(self, frequency):
        return 1

class IdealLowpass(Filter):
    def __init__(self, cutoff):
        self.cutoff = float(cutoff)

    def response(self, frequency):
        if (frequency < self.cutoff):
            return 1
        return 0

class IdealHighpass(Filter):
    def __init__(self, cutoff):
        self.cutoff = float(cutoff)

    def response(self, frequency):
        if frequency < 1:
            return 1
        if (frequency > self.cutoff):
            return 1
        return 0

class GaussLowpass(Filter):
    def __init__(self, cutoff):
        self.cutoff = float(cutoff)

    def response(self, frequency):
        return math.exp(- 0.5 * frequency**2 / self.cutoff**2)


class GaussHighpass(Filter):
    def __init__(self, cutoff):
        self.cutoff = float(cutoff)

    def response(self, frequency):
        if frequency < 0.1:
            return 1
        return 1-math.exp(- 0.5 * frequency**2 / self.cutoff**2)

class ButterworthLowpass(Filter):
    def __init__(self, cutoff, order):
        self.cutoff = float(cutoff)
        self.order = order

    def response(self, frequency):
        return 1.0 / (1 + (frequency / self.cutoff) ** (2 * self.order))


class ButterworthHighpass(Filter):
    def __init__(self, cutoff, order):
        self.cutoff = float(cutoff)
        self.order = order

    def response(self, frequency):
        if frequency < 0.1:
            return 1
        return 1.0 - 1.0 / (1 + (frequency / self.cutoff) ** (2 * self.order))

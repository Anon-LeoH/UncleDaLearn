from Function import *
from Math import *
from Area import *
import random

class distributionObject(mathObject):
    def __init__(self):
        self.type = "distribution"
        self.e = 0
        self.s = 0

    def cal(self, val):
        pass

    def val(self):
        pass

class PointDistribution(distributionObject):
    def __init__(self, point):
        self.value = point
        self.e = self.value
        self.s = 0
    
    def cal(self, val):
        if val == self.value:
            return 1
        else:
            return 0

    def val(self):
        return self.value

class BernoulliDistribution(distributionObject):
    def __init__(self, p):
        self.p = p
        self.e = p
        self.s = 1 - p
    
    def cal(self, val):
        if val == 1:
            return p
        elif val == 0:
            return 1 - p
        else:
            return None
    
    def val(self):
        p = random.random()
        if p > self.p:
            return 0
        else:
            return 1

class BinomialDistribution(distributionObject):
    def __init__(self, p, n):
        self.p = p
        self.n = n
        self.e = n * p
        self.s = n * p * (1 - p)
        self.innerFunc = binomialDisFunction(n, p)
    
    def cal(self, k):
        return self.func.cal(k)

    def val(self):
        rlt = 0
        for i in xrange(self.n):
            tmp = random.random()
            if tmp <= p:
                rlt += 1
        return rlt

class GeometricDistribution(distributionObject):
    def __init__(self, p):
        self.p = p
        self.e = 1 / p
        self.s = (1 - p) / p / p
    
    def cal(self, k):
        return (1 - p) ** (k - 1) * p

    def val(self):
        rlt = 0
        while random.random() > self.p:
            rlt += 1
        return rlt

class PossionDistribution(distributionObject):
    def __init__(self, fy):
        self.fy = fy
        self.e = fy
        self.s = fy
    
    def cal(self, k):
        return (self.fy ** k) * (math.exp( (-1) * self.fy )) / math.factorial(k)

    def val(self):
        rlt = 0
        tmp = self.fy
        while tmp > 0:
            pos = random.random()
            if pos <= tmp:
                tmp -= pos
                rlt += 1
            else:
                tmp = 0
        return rlt

class UniformDistribution(distributionObject):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.e = (a + b) / 2
        self.s = ((b - a) ** 2) / 12

    def cal(self, tp):
        return (tp[1] - tp[0]) / (b - a)

    def val(self):
        return math.uniform(a, b)

class NormalDistribution(distributionObject):
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
        self.e = mu
        self.s = sigma ** 2
        self.innerFunc = GaussianFunction(mu, sigma)

    def cal(self, x):
        return self.innerFunc.cal(x)

    def val(self):
        delta = math.sqrt( (-1) * 2 * (sigma ** 2) * ( 0.5 * math.log(2 * np.pi
        * (sigma ** 2)) + math.log(random.random()) ) )
        return delta + mu

# When I feel that I should add sth. here, I'll add it.

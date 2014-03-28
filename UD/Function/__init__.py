from Area import *
from Math import *
import math
import numpy as np
import random

class functionObject(mathObject):
    def __init__(self):
        self.type = "function"
        self.theta = []
        self.initArea = None
    
    def cal(self, x):
        pass


class constantFunction(functionObject):
    def __init__(self, initArea, value):
        self.initArea = initArea
        self.valueArea = value
    
    def cal(self, x):
        if self.initArea.include(x):
            return self.valueArea
        else:
            return None
    
class linearFunction(functionObject):
    def __init__(self, initArea, theta):
        self.theta = theta
        self.initArea = initArea
    
    def cal(self, x):
        if not isinstance(x, list):
            return None
        if not len(self.theta) == len(x):
            return None
        return sum( [x[i] * theta[i] for i in xrange(len(x))] )

class GaussianFunction(functionObject):
    def __init__(self, mu = 0, sigma = 1, initArea = Area("continous", [[NegIf, PosIf]])):
        self.initArea = initArea
        self.mu = mu
        self.sigma = sigma
    
    def cal(self, x):
        if not isinstance(x, list):
            val = 1.0 / (self.sigma * math.sqrt(2 * np.pi)) * math.exp( (-1) * ((x - self.mu) ** 2) / (2 * (self.sigma ** 2)) )
            return val
        else:
            val = []
            for item in x:
                val.append(self.cal(item))
            return val

class compoundFunction(functionObject):
    def __init__(self):
        pass

    def cal(self, n, k):
        if k < (n / 2):
            k = n - k
        sum1 = 0
        sum2 = 0
        for i in xrange(k+1, n+1):
            sum1 += math.log(i)
        for i in xrange(1, n-k+1):
            sum2 += math.log(i)
        tmp = sum1 - sum2
        return math.exp(tmp)

class binomialDisFunction(functionObject):
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.partFunc = compoundFunction()
    
    def cal(self, k):
        tmpval = self.partFunc.cal(self.n, k)
        return (p ** k) * ((1-p) ** (self.n - k)) * tmpval

class sigmoidFunction(functionObject):
    def __init__(self, theta):
        self.innerFunc = linearFunction([], theta)
    
    def cal(self, x):
        tmp = self.innerFunc.cal(x)
        if tmp == None:
            return tmp
        else:
            return 1 / (1 + math.exp((-1) * tmp))



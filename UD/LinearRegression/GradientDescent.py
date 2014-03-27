from Math import *
from Function import *
from copy import deepcopy as dp
import random
from regularization import regularization as rg

class gradientDescent(functionObject):
    def __init__(self, x, y, alfa, initParam = []):
        functionObject.__init__(self)
        self.rParam, x = rg(x)
        self.rParam = [(0, 1)] + self.rParam
        self.x = []
        for item in x:
            item = [1] + item
            self.x.append(item)
        raw_input("")
        self.y = y
        raw_input("")
        self.m = len(x)
        if len(initParam) != len(self.x):
            initParam = [random.random() for i in xrange(len(self.x[0]))]
        self.param = initParam
        self.alfa = alfa

    def train(self, errorRate):
        realRate = 999
        J1 = PosIf
        J2 = 0
        while realRate >= errorRate:
            tmpParam = dp(self.param)
            J2 = 0
            for j in xrange(len(self.param)):
                sumX = 0
                for i in xrange(self.m):
                    cost = 0
                    for t in xrange(len(self.x[i])):
                        cost += self.x[i][t] * self.param[t]
                    cost -= self.y[i]
                    if j == 0:
                        J2 += cost ** 2
                    sumX += cost * self.x[i][j]
                sumX /= self.m
                tmpParam[j] = tmpParam[j] - self.alfa * sumX
            if J2 > J1:
                raw_input("oops!")
                break
            self.param = tmpParam
            if J1 != PosIf:
                realRate = (J1 - J2) / J2
            J1 = J2
    
    def cal(self, x):
        if not isinstance(x[0], list):
            x = [1] + x
            for i in xrange(len(x)):
                x[i] = (x[i] - self.rParam[i][0]) / self.rParam[i][1]
            return sum( [x[i] * self.param[i] for i in xrange(len(x))] )
        else:
            rlt = []
            for item in x:
                rlt.append(self.cal(item))
            return rlt


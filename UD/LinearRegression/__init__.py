from Area import *
from Math import *
from copy import deepcopy as dp
from regularization import regularization
import random
import math
import numpy as np

class linearRegression(object):
    def __init__(self, trainDataX, trainDataY, dataUse = "all", stepLength = 0.001, initParam = []):
        self.dataX = regularization(trainDataX)
        self.dataY = trainDataY
        if dataUse == "all":
            self.k = len(self.dataX)
        else:
            self.k = dataUse
        self.alfa = stepLength
        if len(initParam) == len(self.dataX[0]):
            self.param = initParam
        else:
            self.param = [random.random() for i in xrange(len(self.dataX[0]))]

    def train(self, error):
        realError = 999
        J1 = 0
        J2 = 0
        ptr1 = 0
        ptr2 = 0
        times = 0
        alfa = self.alfa
        while realError >= error:
            tmpParam = dp(self.param)
            cost = 0
            J2 = 0
            for i in xrange(self.k):
                for t in xrange(len(self.param)):
                    if ptr1 + i >= len(self.dataX):
                        ptr1 -= len(self.dataX)
                    cost += self.dataX[ptr1 + i][t] * self.param[t]
                cost -= self.dataY[i + ptr1]
                J2 += cost ** 2
            ptr1 += self.k
            for j in xrange(len(self.param)):
                xSum = 0
                for i in xrange(self.k):
                    if ptr2 + i >= len(self.dataX):
                        ptr2 -= len(self.dataX)
                    xSum += cost * self.dataX[j][ptr2 + i]
                xSum /= len(self.k)
                alfa = self.alfa * 500 / (times + 500)
                tmpParam[j] = 0.95 * tmpParam[j] - alfa * xSum
            ptr2 += self.k
            self.param = [x for x in tmpParam]
            if J1 > J2:
                realError = (J1 - J2) / J2
            J1 = J2
            times += 1

    def judge(self, x):
        if not isinstance(x[0], list):
            return sum( [x[i] * self.param[i] for i in xrange(len(x))] )
        else:
            tmp = []
            for item in x:
                tmp.append(self.judge(item))
            return tmp

# No test today, I'll do the test tomorrow

from node import *
from LinearRegression.regularization import regularization as rg

class BPnetwork(functionObject):
    def __init__(self, numOfNode):
        if not isinstance(numOfNode, list):
            raise TypeError
        self.nodeList = []
        _id = 0
        for i in xrange(len(numOfNode)):
            label = i
            tmp = []
            l = numOfNode[i]
            if i != len(numOfNode) - 1:
                l += 1
            for j in xrange(l):
                if i == len(numOfNode) - 1:
                    tmpNode = outputNode(_id, label, self.nodeList[i - 1], sigmoidFunction([]))
                elif j == 0:
                    tmpNode = oneNode(_id, label)
                elif i == 0:
                    tmpNode = inputNode(_id, label)
                else:
                    tmpNode = normalNode(_id, label, self.nodeList[i - 1])
                tmp.append(tmpNode)
                _id += 1
            self.nodeList.append(tmp)

    def train(self, xtmp, y, alfa, errorRate):
        self.xParam, x = rg(xtmp)
        j1 = PosIf
        j2 = 0
        realRate = 999
        self.nodeList[0][0].storeVal()
        times = 0
        while realRate >= errorRate:
            times += 1
            alfa = alfa * 5000.0 / (5000 + times)
            for i in xrange(len(x)):
                for j in xrange(len(x[i])):
                    self.nodeList[0][j+1].storeVal(x[i][j])
                for j in xrange(1, len(self.nodeList)):
                    for item in self.nodeList[j]:
                        item.storeVal()
                for j in xrange(len(self.nodeList[-1])):
                    error = y[i][j] - self.nodeList[-1][j].cal()
                    j2 += error ** 2
                    self.nodeList[-1][j].train(error, alfa)
                for j in xrange(len(self.nodeList) - 2, 0, -1):
                    for k in xrange(1, len(self.nodeList[j])):
                        error = 0
                        tp = 0
                        if j != len(self.nodeList) - 2:
                            tp = 1
                        for t in xrange(tp, len(self.nodeList[j+1])):
                            error += self.nodeList[j+1][t].error * self.nodeList[j+1][t].weight[k]
                        self.nodeList[j][k].train(error, alfa)
            j2 = abs(j2)
            if j1 != PosIf:
                realRate = abs(j1 - j2) / j2
            else:
                realRate = 1
            j1 = j2
            j2 = 0

    def cal(self, x):
        self.nodeList[0][0].storeVal()
        x = [(x[i] - self.xParam[i][0]) / self.xParam[i][1] for i in xrange(len(x))]
        for j in xrange(len(x)):
            self.nodeList[0][j+1].storeVal(x[j])
        for j in xrange(1, len(self.nodeList)):
            for item in self.nodeList[j]:
                item.storeVal()
        rlt = []
        for item in self.nodeList[-1]:
            rlt.append(item.cal())
        return rlt


# Haven't test yet.        



from node import *

class BPnetwork(functionObject):
    def __init__(self, numOfNode):
        if not isinstance(numOfNode, list):
            raise TypeError
        self.nodeList = []
        _id = 0
        for i in xrange(len(numOfNode)):
            label = i
            tmp = []
            l = numOfList[i]
            if i != len(numOfList) - 1:
                l += 1
            for j in xrange(l):
                if j == 0 and i != len(numOfList):
                    tmpNode = oneNode(_id, _label)
                elif i == 0:
                    tmpNode = inputNode(_id, label)
                else:
                    tmpNode = normalNode(_id, label, self.nodeList[i - 1])
                tmp.append(tmpNode)
                _id += 1
            self.nodeList.append(tmp)

    def train(self, x, y, alfa, errorRate):
        j1 = PosIf
        j2 = 0
        realRate = 999
        self.nodeList[0][0].storeVal()
        while j1 > j2 and realRate >= errorRate:
            j1 = j2
            j2 = 0
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
                    for k in xrange(len(self.nodeList[j])):
                        error = 0
                        for t in xrange(len(self.nodeList[j+1])):
                            error += self.nodeList[j+1][t].error * self.nodeList[j+1][t].weight[k]
                        self.nodeList[j][k].train(error, alfa)
            realRate = abs(j1 - j2) / j2

    def cal(self, x):
        self.nodeList[0][0].storeVal()
        for j in xrange(len(x[i])):
            self.nodeList[0][j+1].storeVal(x[i][j])
        for j in xrange(1, len(self.nodeList)):
            for item in self.nodeList[j]:
            item.storeVal()
        rlt = []
        for item in self.nodeList[-1]:
            rlt.append(item.cal())
        return rlt


# Haven't test yet.        



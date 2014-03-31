import random
from Function import *
from Distribution import *

class nodeObject(mathObject):
    def __init__(self, _id, _label, connectIn = [], initWeight = []):
        self._id = _id
        self._label = _label
        self.nodeIn = connectIn
        self.error = 0
        if len(initWeight) != len(connectIn):
            initWeight = [random.random() for i in xrange(len(connectIn))]
        self.weight = initWeight

    def train(self):
        pass

    def cal(self):
        pass

class oneNode(nodeObject):
    def __init__(self, _id, _label):
        nodeObject.__init__(self, _id, _label, [], [])

    def storeVal(self):
        self.val = 1

    def cal(self):
        return self.val

class inputNode(nodeObject):
    def __init__(self, _id, _label):
        nodeObject.__init__(self, _id, _label, [], [])

    def storeVal(self, val):
        self.val = val

    def cal(self):
        return self.val

class normalNode(nodeObject):
    def __init__(self, _id, _label, connectIn, func = None, initWeight = []):
        nodeObject.__init__(self, _id, _label, connectIn, initWeight)
        if not func:
            self.innerFunc = sigmoidFunction(self.weight)
        else:
            self.innerFunc = func
            self.innerFunc.setTheta(self.weight)

    def storeVal(self):
        x = []
        for item in self.nodeIn:
            x.append(item.cal())
        self.val = self.innerFunc.cal(x)
    
    def train(self, error, alfa):
        x = []
        for item in self.nodeIn:
            x.append(item.cal())
        self.error = error * self.val * (1 - self.val)
        for i in xrange(len(self.weight)):
            self.weight[i] += alfa * self.error * x[i]
        self.innerFunc.setTheta(self.weight)
        #print str(self._id) + ": " + str(self.weight)

    def cal(self):
        return self.val

class outputNode(nodeObject):
    def __init__(self, _id, _label, connectIn, func, initWeight = []):
        nodeObject.__init__(self, _id, _label, connectIn, initWeight)
        self.innerFunc = func
        self.innerFunc.setTheta(self.weight)
    
    def storeVal(self):
        x = []
        for item in self.nodeIn:
            x.append(item.cal())
        self.val = self.innerFunc.cal(x)

    def train(self, error, alfa):
        x = []
        for item in self.nodeIn:
            x.append(item.cal())
        if isinstance(self.innerFunc, sigmoidFunction):
            self.error = error * self.val * (1 - self.val)
            for i in xrange(len(self.weight)):
                self.weight[i] += alfa * self.error * x[i]
        else:
            self.error = (-1) * error
            for i in xrange(len(self.weight)):
                self.weight[i] = 0.9 * self.weight[i] + alfa * self.error * x[i]
        
        self.innerFunc.setTheta(self.weight)
        #print str(self._id) + ": " + str(self.weight)

    def cal(self):
        return self.val
        

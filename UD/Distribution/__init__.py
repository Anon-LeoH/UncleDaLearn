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
		self.func = binomialDisFunction(n, p)
	
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
		return (1 - p) ^^ (k - 1) * p

	def val(self):
		rlt = 0
		while random.random() > self.p:
			rlt += 1
		return rlt

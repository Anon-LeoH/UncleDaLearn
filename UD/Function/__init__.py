from .. import Area
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
	def __init__(self, initArea = Area("continous", [[NegIf, PosIf]]), mu = 0, sigma = 1):
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


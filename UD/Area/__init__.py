from Math import mathObject
import random

class areaObject(mathObject):
	def __init__(self):
		self.type = "Area"
		self.areaType = None
		self.pieces = []
		self.content = []
	
	def include(self, x):
		pass

class areaPiece(areaObject):
	def __init__(self, content, tp):
		self.areaType = tp
		if isinstance(content, list):
			self.content = content
		else:
			self.content = [content]
	
	def include(self, x):
		if isinstance(x, list):
			if self.areaType == "discrete":
				for item in x:
					if not item in self.content:
						return False
				return True
			elif self.areaType == "continous":
				for item in x:
					if not self.content[0] <= item <= self.content[1]:
						return False
				return true
			else:
				return False
		elif isinstance(x, int) or isinstance(x, float):
			if self.areaType == "discrete":
				if not x in self.content:
					return False
				else:
					return True
			elif self.areaType == "continous":
				if not self.content[0] <= x <= self.content[1]:
					return False
				else:
					return True
			else:
				return False
		elif isinstance(x, mathObject) or isinstance(x, object):
			if self.areaType != "discrete" and self.areaType != "continous":
				return False
			if isinstance(x, areaObject):
				if isinstance(x, areaPiece):
					if x.areaType == "continous" and self.areaType == "discrete":
						return False
					else:
						return self.include(x.content)
				else:
					rlt = True
					for item in x.pieces:
						rlt = rlt and self.include(item)
					return rlt
			else:
				if self.areaType != "discrete":
					return False
				else:
					if x in self.content:
						return True
					else:
						return False
		else:
			return False

class Area(areaObject):
	def __init__(self, tp, thetaList):
		if isinstance(thetaList):
			tmp = []
			for item in thetaList:
				if isinstance(item, list):
					self.pieces.append(areaPiece(item, tp))
		else:
			self.pieces.append(areaPiece(thetaList, tp))
		self.areaType = tp
	
	def include(self, x):
		for piece in self.pieces:
			if piece.include(x):
				return True
		return False



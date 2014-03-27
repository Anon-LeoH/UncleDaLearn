from LinearRegression.HugeScaleLR import hugeScaleLR as hlr
from LinearRegression.GradientDescent import gradientDescent as glr
import numpy as np
from copy import deepcopy as dp
import random
import math
from Function import *
from Distribution import NormalDistribution as nd
import matplotlib.pyplot as plt

fig = plt.figure()  
fig.suptitle(u'Informations gragh paramed by level', fontsize=14, fontweight='bold')  
ax = fig.add_subplot(111)

error = nd(0, 0.5)

class testFunc(functionObject):
	def __init__(self):
		pass

	def cal(self, x):
		return ( 0.7 * x - 7 * (x ** 2) + 0.1 * (x ** 3) + 7 )

tf = testFunc()
x = []
y = []

for i in xrange(0, 2000):
	tmp = [(i / 100.0) * 1, (i / 100.0) ** 2, (i / 100.0) ** 3]
	x.append(tmp)
	y.append(tf.cal(i / 100.0))

x1 = dp(x)
y1 = dp(y)
jg1 = glr(x, y, 0.009)
jg2 = hlr(x1, y1, 0.009, 10)

jg1.train(0.00001)
jg2.train(0.00001)

for i in xrange(10):
	tmp = random.uniform(0.1, 25.0)
	ty1 = tf.cal(tmp)
	tmp = [tmp * 1, tmp ** 2, tmp ** 3]
        tmp1 = dp(tmp)
	ty2 = jg1.cal(tmp)
        ty3 = jg2.cal(tmp1)
	rlt = (ty1, ty2, ty3)
	print rlt

x = np.arange(0.0, 25.0, 0.01)
y1 = [tf.cal(item) for item in x]
y2 = [jg1.cal([item, item ** 2, item ** 3]) for item in x]
y3 = [jg2.cal([item, item ** 2, item ** 3]) for item in x]

ax.plot(x, y1, 'r', x, y2, 'b', x, y3, 'y')

fig.savefig('level.png', dpi=100)
fig.show()



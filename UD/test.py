from LinearRegression.HugeScaleLR import hugeScaleLR as hlr
from LinearRegression.GradientDescent import gradientDescent as glr
from LinearRegression.regularization import regularization as rg
import numpy as np
from copy import deepcopy as dp
import random
import math
from Function import *
from Distribution import NormalDistribution as nd
import matplotlib.pyplot as plt
from NeuralNetwork import BPnetwork as bpn

fig = plt.figure()  
fig.suptitle(u'Informations gragh paramed by level', fontsize=14, fontweight='bold')  
ax = fig.add_subplot(111)

set11 = nd(3, 2.5)
set12 = nd(3, 2.5)
set13 = nd(3, 2.5)
set21 = nd(-6, 1.0)
set22 = nd(-6, 1.0)
set23 = nd(-6, 1.0)

class testFunc(functionObject):
	def __init__(self):
		pass

	def cal(self, x):
		return ( 0.7 * x - 7 * (x ** 2) + 0.1 * (x ** 3) + 7 )

tf = testFunc()
x = []
y = []
y2 = []

for i in xrange(1000):
	x.append([set11.val(), set12.val(), set13.val()])
        y.append([1, 0])

for i in xrange(1000):
	x.append([set21.val(), set22.val(), set23.val()])
        y.append([0, 1])

y2 = [[item] for item in y2]
jg = bpn([3, 4, 4, 2])

jg.train(x, y, 0.03, 0.0005)

#for i in xrange(10):
#	tmp = random.uniform(0.1, 25.0)
#	ty1 = tf.cal(tmp)
#	tmp = [tmp * 1, tmp ** 2, tmp ** 3]
#        tmp1 = dp(tmp)
#	ty2 = jg1.cal(tmp)[0]
#        ty3 = jg2.cal(tmp1)
#        ty2 = ty2 * param[1] + param[0]
#	rlt = (ty1, ty2, ty3)
#	print rlt

#x = np.arange(-20.0, 20.0, 0.01)
#y1 = [tf.cal(item) for item in x]
#y2 = [jg1.cal([item, item ** 2, item ** 3])[0] * param[1] + param[0] for item in x]
#y3 = [jg2.cal([item, item ** 2, item ** 3]) for item in x]

#ax.plot(x, y1, 'r', x, y2, 'b', x, y3, 'y')

#fig.savefig('level.png', dpi=100)
#fig.show()

tr = 0
fl = 0

for i in xrange(100):
    p = random.random()
    if p >= 0.5:
        tmpx = [set11.val(), set12.val(), set13.val()]
        tmpy = 1
    else:
        tmpx = [set21.val(), set22.val(), set23.val()]
        tmpy = 2
    rlt = jg.cal(tmpx)
    if rlt[0] > rlt[1]:
        rlt = 1
    else:
        rlt = 2
    if rlt == tmpy:
        tr += 1
    else:
        fl += 1

print "result: " + str(float(tr) / (tr + fl))

    


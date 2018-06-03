#calculate using the entropy formula and python's math module
import math
print -0.67*math.log(0.67, 2) - 0.33*math.log(0.33, 2)

#calculate using scipy.stats module
import scipy.stats
print scipy.stats.entropy([2,1],base=2)

__author__ = 'pallavipriya'

import random

iter = 10000
count = 0
x = []
y = []

for i in range(iter):
    x.append(random.uniform(-1,1))
    y.append(random.uniform(-1,1))

for i,j in zip(x,y):
    if ((i*2)+(j*2)) <=1:
        count +=1

print 4 * count/float(iter)


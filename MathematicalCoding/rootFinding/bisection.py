__author__ = 'pallavipriya'
import math

precison = .001

def bisectionMethod(func,a,b):

    mid = (a + b)/2
    if func(a) * func(b) <= 0:
        while func(mid) <= precison:
            if func(a) * func(mid) <= 0:
                b = mid
            else:
                a = mid
        mid = (a + b) / 2
    return mid

def func(x):
    return math.cos(x)

mymethod = bisectionMethod(func,1,2)
print mymethod



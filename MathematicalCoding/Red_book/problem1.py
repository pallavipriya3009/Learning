__author__ = 'pallavipriya'

import math

def integration(fun,a,b):
    n = 10000.0
    deltax = (b-a)/n
    sum = 0
    x = a
    while x <= b:

        sum = sum + func(x) * deltax
        x = x + deltax

    return sum

def func(x):
    return math.exp(-1*x**2)

print integration(func,-10000,10000)
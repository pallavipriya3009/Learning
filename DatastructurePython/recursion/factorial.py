__author__ = 'pallavipriya'

def factorial(n):
    if n < 2:
        return 1
    else:
        return factorial(n-1) * n

print factorial(6)
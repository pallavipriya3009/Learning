__author__ = 'pallavipriya'

def fibonacci(n):
    if n<=1:
        return 1
    while n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(4)
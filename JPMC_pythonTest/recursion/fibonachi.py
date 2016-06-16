__author__ = 'pallavipriya'


def fibonachi(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)

print(fibonachi(6))
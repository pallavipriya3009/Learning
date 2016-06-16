__author__ = 'pallavipriya'
fibdict = {}

def fibonacci(n):
    if n in fibdict:
        return fibdict[n]
    else:
        if n<1:
            fibdict[n] = 0
        elif 1<=n<2:
            fibdict[n] = 1
        else:
            fibdict[n] = fibonacci(n-1) + fibonacci(n-2)

        return fibdict[n]

print fibonacci(4)
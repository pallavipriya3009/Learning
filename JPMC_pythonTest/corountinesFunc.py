__author__ = 'pallavipriya'

def func():
    alist =[]
    while True:
        alist.append((yield))
        print(alist)

f = func()
f.next()
f.send(6)
f.send(3)

__author__ = 'pallavipriya'

def test(n):
        while n >0:
            yield n
            n -=1
try:
    t = test(4)
    print(t.next())
    print(t.next())
    print(t.next())
    print(t.next())
    print(t.next())
except StopIteration:
    print("The exception caught")










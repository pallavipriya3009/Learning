__author__ = 'pallavipriya'

def func(n):

    i = 0
    while i < n:
        print("before",i)
        yield i
        print("after",i)
        i +=1


f  = func(5)
print(f.next())
print(f.next())
"""print(f.next())
print(f.next())
print(f.next())"""

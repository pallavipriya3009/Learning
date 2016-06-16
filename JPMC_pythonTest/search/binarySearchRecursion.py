__author__ = 'pallavipriya'

def binarySearchRecursion(value,L):
    if len(L) <1:
        print ("Not found")
    else:
        mid = len(L) / 2
        if value < L[mid]:
            binarySearchRecursion(value,L[:mid])
        elif value > L[mid]:
            binarySearchRecursion(value,L[mid+1:])
        elif value == L[mid]:
            print "value found at index {0}".format(mid)

binarySearchRecursion(10,L=[1,2,3,5,9])



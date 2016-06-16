__author__ = 'pallavipriya'

def insertionSort(L):

    length = len(L)

    for i in range(length):
        for j in range(i-1,0,-1):
            if L[j+1] < L[j]:
                L[j+1],L[j] = L[j],L[j+1]

    return "The sorted array is :{}".format(L)

print(insertionSort([1,4,2,6,3]))
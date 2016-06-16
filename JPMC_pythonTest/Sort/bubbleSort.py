__author__ = 'pallavipriya'

def bubbleSort(L):
    length = len(L)
    for i in range(length-1):
        for j in range(i,length-1):
            if L[j] > L[j + 1]:
                L[j],L[j+1] = L[j+1],L[j]
    return "The sorted array is : {}".format(L)


print(bubbleSort(L=[1,4,2,8,3]))
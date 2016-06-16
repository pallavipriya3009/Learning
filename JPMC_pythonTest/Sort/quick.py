__author__ = 'pallavipriya'

def quickSort(L,start,end):
    if start>end:
        return
    else:
        Index = partition(L,start,end)
        quickSort(L,start=start,end=Index-1)
        quickSort(L,start=Index+1,end=end)
    return L

def partition(L,start,end):
    pIndex = start
    pivot = L[end]
    for i in range(start,end):
        if L[i] <= pivot:
            L[i],L[pIndex] = L[pIndex],L[i]
            pIndex = pIndex +1
    L[end],L[pIndex] = L[pIndex],L[end]
    return pIndex

inputlist=[1,4,2,6,3]
print (quickSort(inputlist,start=0,end=len(inputlist)-1))


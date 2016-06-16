__author__ = 'pallavipriya'

def mergeSort( arr, start, end ):
    if end-start<=0:
        return None
    mid = (start+end)/2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid+1, end)
    merge(arr, start, mid, end)

def merge( arr, start, mid, end ):
    tarr = []
    i, j = start, mid+1
    while i<=mid and j<=end:
        if arr[i]<=arr[j]:
            tarr.append( arr[i] )
            i+=1
        else:
            tarr.append( arr[j] )
            j+=1
    while i<=mid:
        tarr.append( arr[i] )
        i+=1
    while j<=end:
        tarr.append( arr[j] )
        j+=1
    arr[ start:end+1 ] = tarr

L = [1,4,2,6,3,10,-1,8,5,9,7,-2]
print( 'Input:  ', L )
mergeSort(L,0,len(L)-1)
print( 'Output: ', L )
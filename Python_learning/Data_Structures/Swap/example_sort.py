__author__ = 'pallavipriya'

def reverse(arr):
    length = len(arr)
    for itr in range(int(length/2)):
        (arr[itr],arr[length-1-itr]) = (arr[length-1-itr],arr[itr])





arr = [1,4,2,8,5]
reverse(arr)
print (arr)
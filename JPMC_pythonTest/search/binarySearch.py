__author__ = 'pallavipriya'

def binarySearch(value):
    L = [1,8,2,7,10]
    length = len(L)

    start = 0
    end = length-1
    mid = (start + end) / 2
    for itr in range(length):
        if value < L[mid]:
            end = mid -1
        elif value > L[mid]:
            start = mid + 1
        else:
            return "value found at index {}".format(mid)
        mid = (start + end) / 2

print(binarySearch(10))
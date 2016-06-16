__author__ = 'pallavipriya'

def binarySearch(value):

    #inputlist = [2,-1,0,7,5,9,6]
    inputlist = [1,3,2,4,5,6,7,11,12]
    sortedlist = sorted(inputlist)
    print sortedlist
    start = 0
    end = len(sortedlist)-1
    mid = (start + end) /2
    while mid > start:
        if value < sortedlist[mid]:
            end = mid
            mid = (start + end) / 2
        else:
            start = mid
            mid = (start + end) / 2

        if value == sortedlist[mid]:
            print "value found at index {0}".format(mid)
            return

    print "Value not found in the given list"

binarySearch(4)




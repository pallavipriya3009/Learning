__author__ = 'pallavipriya'

def mergesort(inputlist):
    length = len(inputlist)
    mid = length // 2
    aleft = inputlist[:mid]
    bright = inputlist[mid:]

    if length < 2:
        return
    else:
        mergesort(aleft)
        mergesort(bright)
    merge(inputlist,aleft,bright)
    return inputlist

def merge(alist,llist,rlist):
    i = 0
    j = 0
    k = 0
    length = len(alist)
    nl = len(llist)
    nr = len(rlist)
    while i < nl and j < nr:
        if llist[i] <= rlist[j]:
            alist [k] = llist[i]
            i +=1
        else:
            alist[k] = rlist[j]
            j+=1
        k+=1
    while i<nl:
        alist[k] = llist[i]
        i+=1
        k+=1
    while j<nr:
        alist[k] = rlist[j]
        j+=1
        k+=1

mylist = [2,4,-1,6,-8,5,0,7,9]
print mergesort(mylist)
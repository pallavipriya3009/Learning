__author__ = 'pallavipriya'

def quickSort(inputlist,start,end):
    if start<end:
        partindex = partition(inputlist,start,end)
        #print inputlist
        quickSort(inputlist,start=start,end=partindex-1)
        quickSort(inputlist,start=partindex+1,end=end)
    return inputlist

def partition(inputlist,start,end):
    print start, end, inputlist[start:end+1]
    pivot = inputlist[end]
    partindex = start
    for i in range(start, end):
        if inputlist[i] <= pivot:
            temp = inputlist[i]
            inputlist[i] = inputlist[partindex]
            inputlist[partindex] = temp
            partindex +=1
    temp = inputlist[end]
    inputlist[end] = inputlist[partindex]
    inputlist[partindex] = temp
    return partindex


mylist = [2,4,-1,0,8,3]
print quickSort(mylist,0,len(mylist)-1)


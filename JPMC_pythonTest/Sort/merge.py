__author__ = 'pallavipriya'


def mergeSort(alist):
    mid = len(alist)// 2
    Llist = []
    Rlist = []
    if len(alist) <2:
        return
    else:
        for i in range(mid):
            Llist.append(alist[i])
        for j in range(mid,len(alist)):
            Rlist.append(alist[i])
        mergeSort(Llist)
        mergeSort(Rlist)
    merge(Llist,Rlist,alist)
    return alist

def merge(Llist,Rlist,alist):
    i=0;j=0;k=0
    while i < len(Llist) and j <len(Rlist):
        if Llist[i] < Rlist[j]:
            alist[k]=Llist[i]
            i +=1
        else:
            Llist[i] > Rlist[j]
            alist[k]=Rlist[j]
            j +=1
        k +=1

    while i<len(Llist):
        alist[k]=Rlist[i]
        i+=1
        k+=1
    while j<len(Rlist):
        alist[k]=Llist[j]
        j+=1
        k+=1



print(mergeSort([1,4,2,6,3]))



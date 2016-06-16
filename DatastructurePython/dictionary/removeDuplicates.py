__author__ = 'pallavipriya'

def removeDuplicateInorder(blist):
    adict = {}
    alist = []
    for item in blist:
        if item not in adict:
            adict[item] = None
            alist.append(item)
    return alist

blist = [2,4,-1,5,6,1,0,2,3,0]

print removeDuplicateInorder(blist)



__author__ = 'pallavipriya'

def reverseRecursionStr(istring):

    # changedStr = list(istring)
    # alist = []
    # if len(changedStr) <1:
    #     return
    # else:
    #     alist.append(changedStr)
    #     reverseRecursionStr(istring[1:])
    #     return alist
    if len(istring)==1:
        return istring
    pivot   = istring[0]
    nextrev = reverseRecursionStr( istring[1:] )
    return nextrev+pivot

print(reverseRecursionStr("character"))
__author__ = 'pallavipriya'

"""How to convert numeric String to an int? """

def strToInt(astring):
    alist = list(astring)
    blist = []
    for itr in range(len(alist)):
        blist.append((ord(alist[itr])-48) * (10 ** (len(alist)-itr -1)) )
    return sum(blist)

print(strToInt("12345"))
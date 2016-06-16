__author__ = 'pallavipriya'

"""How to find duplicate characters in a String?"""

def dupliChar(inputString):

    length = len(inputString)
    ddict = {}
    for itr in range(length):
        ddict.setdefault(inputString[itr],0)
        ddict[inputString[itr]] += 1
    return [k for k,v in ddict.items() if v>1 ]

print dupliChar("character")
__author__ = 'pallavipriya'

"""How to program to print first non repeated character from String?"""


def nonRepeatedChar(astring):
    ddict = {}

    for item in astring:
        if item not in ddict.keys():
            ddict[item] = 1
        else:
            ddict[item] +=1
    for itr in astring:
        if ddict[itr] == 1:
            return "First non repeated character {} found!".format(itr)

print(nonRepeatedChar("character"))




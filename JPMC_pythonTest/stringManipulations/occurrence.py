__author__ = 'pallavipriya'

"""How to count occurrence of a given character in String?"""

def occurranceValue(astring,value):
    ddict = {}
    for itr in astring:
        ddict.setdefault(itr,0)
        ddict[itr] +=1

    if value in ddict.keys():
        return "The character '{0}' in the string '{1}' has occurred {2} times".format(value,astring,ddict[value])
    else:
        return "The character not found in the string"

print(occurranceValue("pallavipriya","a"))
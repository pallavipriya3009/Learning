__author__ = 'pallavipriya'

def linearSearch(val):
    l = [1,4,2,9,10]
    length = len(l)

    for itr in range(length):
        if val == l[itr]:
            return "Value found at index {} in the list.".format(itr)
    return None

print(linearSearch(2))




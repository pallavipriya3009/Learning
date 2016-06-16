__author__ = 'pallavipriya'

def linearsearch(value):
    inputlist = [2,-1,0,7,3,9,6]

    for i in range(len(inputlist)):
        if value == inputlist[i]:
            print "The value found in the list is at index {}".format(i)

linearsearch(6)
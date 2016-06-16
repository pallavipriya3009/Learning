__author__ = 'pallavipriya'

"""How to reverse String in Java using Iteration"""

def reverseItrStr(istring):
    changedStr = list(istring)
    length = len(changedStr) -1

    for itr in range(0,len(changedStr)/2):
        changedStr[itr],changedStr[length-itr] =  changedStr[length-itr],changedStr[itr]
    return "".join(changedStr)

str = "retcarahc"
print(reverseItrStr(str))
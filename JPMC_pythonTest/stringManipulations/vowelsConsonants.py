__author__ = 'pallavipriya'

""" How to count number of vowels and consonants in a String?"""

def vowConso(astring):
    vcount = 0;ccount = 0
    for item in astring:
        if item in {'a','e', 'i','o','u'}:
            vcount +=1
        else:
            ccount +=1
    return "The total number of vowels and consonants in the string '{0}' are {1} and {2}".format(astring,vcount,ccount)

print(vowConso("character"))
__author__ = 'pallavipriya'

"""How to check if two Strings are anagrams of each other? """


def anagrams(istring,bstring):

    astr = sorted((istring.lower()))
    bstr = sorted(bstring.lower())

    if len(astr) != len(bstr):
        return ("string are not anagram of each other")
    else:
        for i,j in zip(astr,bstr):
            if i!=j:
                return "string are not anagram of each other"
            else:
                return "string are anagram of each other"

print(anagrams("character","cHraaCter"))
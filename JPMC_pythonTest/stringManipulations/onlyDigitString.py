__author__ = 'pallavipriya'

"""How to check if a String contains only digits?"""


def ifString(istring):
    for itr in range(len(istring)):
        try:
            if int(istring[itr],base=10) < 9:
                pass
            return " The string contains only integer"

        except ValueError as e:
            return ("The string contains character {} ".format(istring[itr]))

print(ifString("12545"))
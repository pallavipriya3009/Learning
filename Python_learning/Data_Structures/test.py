__author__ = 'pallavipriya'

def raiseExcept(num):
    """
    This is a function that takes only positive numbers
    :param num:
    :return: positive number or raises IOError
    """
    if num < 0:
        raise IOError("Input number greater than zero")
    else:
        return num

#print(raiseExcept(-1))
arr = [4,-1,5,6]

print( raiseExcept.__doc__ )
raiseExcept.__doc__ = "Overridden"
print( raiseExcept.__doc__ )
for itr in arr:
    try:
        print(raiseExcept(itr))
    except Exception as e:
        print(e)




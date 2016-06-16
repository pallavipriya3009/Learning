__author__ = 'pallavipriya'

def pow(a,b):
    result =1
    if a == 0:
        if b <0:
            raise ZeroDivisionError
        elif b >0:
            return 0
        else:
            return 1
    else:

        if a >0 and b >0:
            for itr in range(1,b+1):
                result = result * a
            return result
        elif a<0 and b>0:
            for itr in range(1,b+1):
                result = result * a
            return (result)

        elif a<0 and b<0:
            for itr in range(1,abs(b)+1):
                result = result * a
            return (1/float(result))
        else:
            for itr in range(1,abs(b)+1):
                result = result * a
            return   (1/float(result))



print(pow(2,-5))





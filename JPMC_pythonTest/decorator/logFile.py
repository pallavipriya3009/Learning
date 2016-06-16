__author__ = 'pallavipriya'

f = open("abc.txt","w")

def log(func):
    def fun(x):
        f.write("input : {} \n".format(x))
        f.write("output : {} \n\n".format(func(x)))
        return func(x)
    return fun


@log
def sqFunc(x):
    return x **2

print(sqFunc(2))
sqFunc(5)
sqFunc(9)

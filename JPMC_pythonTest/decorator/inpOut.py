__author__ = 'pallavipriya'


def d_decorator(func):
    def foo(name):
        print("Before call {}".format(name))
        print("after  call {}".format(func(name)))
        #print "After decoration the return is {}".format(func(name))
    return foo

@d_decorator
def fun(name):
    return name + "bhagwan"

fun("krishna")
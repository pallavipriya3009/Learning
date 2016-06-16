__author__ = 'pallavipriya'
enable_Tracing = True
if enable_Tracing:
    debug_log = open('debug.log','w')

def trace(func):
    if enable_Tracing:
        def callf(*args,**kwargs):
            debug_log.write("calling %s %s \n" % (args,kwargs))
            r = func(*args,**kwargs)
            debug_log.write("{} returned {}".format(func.__name__,r))
            return r
        return callf
    else:
        return func
@trace
def square(a,b,name=""):
    return "{} is friend of {},{}".format(name,a,b)

print(square("pallavi","priya",name="parivesh"))

from listoffuncs import Func21, Func321

def bisection( a, b, f ):
    # find root
    return f( b )

if __name__=='__main__':
    print 'root of Func21 is: {0}'.format( bisection( -100, 100, Func21 ) )
    print 'root of Func321 is: {0}'.format( bisection( -100, 100, Func321 ) )
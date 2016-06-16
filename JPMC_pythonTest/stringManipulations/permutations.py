__author__ = 'pallavipriya'

def permutations(astring):

    if len(astring)<1:
        return None
    if len(astring)==1:
        return [astring]
    else:
        alist = []
        for i in range(len(astring)):
            pivot     = astring[i]
            topermute = astring[:i]+astring[i+1:]
            piter     = permutations(topermute)
            # for iter in piter:
            #     alist.append(pivot+iter)
            # print( 'pivot={0}, topermute={1}, piter={2}, alist{3}'.format(
            #         pivot, topermute, piter, alist) )
        return alist

print(permutations("abcd"))
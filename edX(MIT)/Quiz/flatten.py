def flatten(lst):
    flattened=[]
    print( 'argument to main loop:', lst)
    for i in lst:
        if  isinstance(i, list):
            for j in i:
                print ('passing %r for nested lists' % j)
                if isinstance(j, list):
                    flattened+=flatten(j)
                else:
                    flattened.append(j)
        else:
            flattened.append(i)
    return flattened

print (flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
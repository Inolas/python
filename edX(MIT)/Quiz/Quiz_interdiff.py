def f(a,b):
    return a>b
def dict_interdiff(d1, d2):
    di2,di1={},{}
    for i in d1:
        if i in d2:
            di1[i]=f(d1[i],d2[i])
        else:
            di2[i]=d1[i]

    for j in d2:
        if j not in d1:
            di2[j]=d2[j]
    return (di1,di2)

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print(dict_interdiff(d1,d2))

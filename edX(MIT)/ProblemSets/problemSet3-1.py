def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start,stop,step):
    if(start<stop):
        return (f(start)*step)+radiationExposure(start+step,stop,step)
    else:
        return 0
start=0
stop=11
step=1
print (radiationExposure(start,stop,step))

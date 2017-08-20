num = raw_input('ENTER AN INTEGER')
if(num<0):
    num = abs(num)
    isNeg = True
else:
    isNeg = False
result =''
if(num==0 | int(num)==1):
    result = num
while(num>0):
    result = str(num%2) + result
    num = num/2
if(isNeg):
    result = '-'+result
print result

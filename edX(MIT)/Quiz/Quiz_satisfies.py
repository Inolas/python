def f(s):
  return 'a' in s

def satisfiesF(L):
  count= len(L)
  rec_list=list()
   
  for i in range(0,count):
    if(f(L[i])==False):
      rec_list.append(L[i])
  if(rec_list):
    for j in rec_list:
      L.remove(j)
  return len(L)

L = ['a', 'b', 'a']
print (satisfiesF(L))
print (L)

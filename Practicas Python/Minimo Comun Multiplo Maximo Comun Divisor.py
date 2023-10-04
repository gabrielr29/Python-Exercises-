import math

def mincm(a, b):
    
  return (a*b)/math.gcd(a,b)

def maxcm(a,b):
  m = min(a,b)

  for i in range(1,m+1):
    if (a%i == 0 and b%i==0):
        MCD = i
  return MCD 


a = mincm(2,4)

print (a)
print(maxcm(44,66))
print(math.gcd(44,66))


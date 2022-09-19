# Say the prime factorization of a number is 2^n * 3^p * 5^q * ..., the total number of factors is (n+1)*(p+1)*(q+1)
# This is because there are n+1 different 2^i combinations which each provide a unique factor. Same with p+1 possibilities for 3^i
# multiply them all and we get the above formula

from collections import Counter

def numfactors(num):
  n = num
  factorlist = Counter()
  while n%2 == 0:
    factorlist[2] += 1
    n/=2

  i=3
  while i <= n:
    while n%i == 0:
      factorlist[i] += 1
      n/=i
    i+=2
  prod = 1
  for factor, power in factorlist.items():
    prod*=(power+1)
  return prod

i=2
factorcount = 0
maxfactorcount = 500

while factorcount < maxfactorcount:
  triangle = i*(i+1)/2
  i+=1
  factorcount = numfactors(triangle)
  if factorcount > maxfactorcount:
    print triangle
    break

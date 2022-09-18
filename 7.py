def isPrime(n):
    if n%2==0:
        return True
    if n in [2,3,5,7,11,13]:
        return True
    start = 3
    while start*start <= n:
        if n%start == 0:
            return False
        start+=2
    return True

primecount = 1
cand = 3
while primecount < 10001:
    if isPrime(cand):
        primecount += 1
        print cand, primecount
    cand+= 2
print cand-2


        
print isPrime(2)
print isPrime(3)
print isPrime(37)
print isPrime(39)

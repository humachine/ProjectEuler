qn = 2000000
sieve = {i:True for i in range(3, qn, 2)}
primesum = 2
for cand in range(3, qn, 2):
    if sieve[cand] == True:
        for i in range(cand*3, qn, cand*2):
            sieve[i] = False
        primesum+=cand
print primesum

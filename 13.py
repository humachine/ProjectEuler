from collections import Counter
maxnum = 1000000
collatzlen = {i:0 for i in range(maxnum)}
collatzlen[1] = 1

def seqlength(num):
  if collatzlen.get(num,0) > 0:
    return collatzlen[num]
  if num%2 == 0:
    collatzlen[num] = 1+seqlength(num/2)
  else:
    collatzlen[num] = 1+seqlength(3*num+1)
  return collatzlen[num]

maxlen = 1
culprit = 1
for i in range(1, maxnum):
  seqlen = seqlength(i)
  if seqlen > maxlen:
    maxlen, culprit = seqlen, i
print maxlen, culprit

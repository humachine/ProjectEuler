# (a+b+c+...n)^2 = a^2 + b^2 + ... + n^2 + 2a(b+c+..+n) + 2b(c+d+..+n) + ... 2mn
# 101000 - (i^2+i)/2

n = 100
ans = 0
for i in range(1,100):
    subsum = 5050 - (i*i+i)/2
    ans += 2*i*subsum
    print i, subsum
print ans

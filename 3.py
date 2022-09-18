num = 600851475143

i,n = 3,num

ans = set()
while i*i < num: 
    while n%i == 0:
        print i, 'divides'
        ans.add(i)
        n/=i
    i+=2
print ans

prev = 1
curr = 2
ans = 0
while curr < 4000000:
    if curr%2 == 0:
        ans+=curr
    prev, curr = curr, curr+prev
print ans

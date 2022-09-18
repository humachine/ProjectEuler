ans = 3
mult = (1,3)
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        if i%11 >0 and j%11>0:
            continue
        prod = str(i*j)
        if prod == prod[::-1]:
            if i*j > ans:
                ans = i*j
                mult = (i,j)
print ans, mult

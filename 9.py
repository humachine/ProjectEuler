a = 1-332
for a in range(332):
    maxb = (1000-a)/2
    for b in range(a, maxb): 
        c = 1000-a-b
        if a*a == (c+b)*(c-b):
            print a*b*c
            break



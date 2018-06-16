t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split()
    n,c,m = [int(n),int(c),int(m)]
    ini=n//c
    count=ini
    while ini>=m:
        ini-=m
        ini+=1
        count+=1
    print(count)
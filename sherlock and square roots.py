import math
t=int(input())
while t>0:
    n,m=input().strip().split()
    n,m=[int(n),int(m)]
    count = math.floor(math.sqrt(m)) - math.floor(math.sqrt(n - 1))
    t-=1
    print(count)
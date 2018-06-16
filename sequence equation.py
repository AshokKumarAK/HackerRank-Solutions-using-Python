n=int(input())
p=[int(a) for a in input().split()]
for i in range(1, n+1):
    print(p.index(p.index(i)+1)+1)
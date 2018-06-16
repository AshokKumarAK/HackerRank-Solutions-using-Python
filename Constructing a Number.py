q=int(input())
for i in range(q):
    n=int(input())
    a=[int(j) for j in input().split()]
    if sum(a) % 3==0:
        print("YES")
    else:
        print("NO")
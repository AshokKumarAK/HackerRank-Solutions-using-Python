t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a) for a in input().strip().split()]
    count=0
    for i in a:
        if i<=0:
            continue
        else:
            count+=1
    pre=n-count
    print(pre)
    if pre>=k:
        print("No")
    else:
        print("YES")
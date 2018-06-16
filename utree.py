t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    count=1
    if n==0:
        print(count)
    elif n==1:
        print(count+1)
    else:
        for i in range(1,n+1):
            if i%2!=0:
                count=count*2
            else:
                count=count+1
        print(count)


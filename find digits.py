t = int(input().strip())
for a0 in range(t):
    count=0
    n = input().strip()
    div=[int(d) for d in str(n)]
    for i in div:
        if i==0:
            pass
        elif int(n)%i ==0:
            count+=1
    print(count)
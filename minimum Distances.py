n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
b=set(A)
ans=max(A)
c=0
for i in b:
    if A.count(i)>=2:
        ans=min(ans,abs((A.index(i))-(len(A)-A[::-1].index(i)-1)))
    else:
        c+=1
if(c==len(A)):
    print(-1)
else:
    print(ans)
i,j,k=input().split()
i,j,k=[int(i),int(j),int(k)]
count=0
for a in range(i,j+1):
    b=int(str(a)[::-1])
    if (a-b)%k==0:
        count+=1
print(count)
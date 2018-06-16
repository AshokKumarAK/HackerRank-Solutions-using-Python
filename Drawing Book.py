n=int(input())
p=int(input())
count=0
cou=0
for i in range(1,n,2):
    if i==p or i-1==p:
        break
    count+=1
if n%2!=0:
    for i in range(n,1,2):
        if i==p or i-1 ==p:
            break
        cou+=1
else:
    for i in range(n-1,1,-2):
        if i==p or i-1==p:
            break
        cou+=1
if n==p:
    print(0)
elif count<cou:
    print(count)
else:
    print(cou)


n=int(input())
s=[]
tem=0
count=0
for _ in range(n):
    t=int(input())
    s.append(t)
print(s)
d=int(input())
m=int(input())
sum=0
for i in range(n):
    j=0
    lim=i+m
    i+=1
    if lim>n:
        break
    while j<lim:
        sum+=s[j]
    if sum==d:
        count+=1
print(count)
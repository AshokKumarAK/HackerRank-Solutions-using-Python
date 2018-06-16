n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
d=set(c)
ans=0
for i in range(len(d)):
    t=c.count(d[i])
    if t>ans:
        ans=t
print(len(c)-ans)

n=int(input())
k=int(input())
a=[]
count=0
for _ in range(n):
    t=int(input())
    a.append(t)
for i in range(n):
    for j in range(n):
        if i<j:
            tem = a[i] + a[j]
            if tem % k == 0:
                count += 1
print(count)
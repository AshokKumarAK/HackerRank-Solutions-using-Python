n=int(input())
count=0
p=5
for _ in range(1,n+1):
    inter=p//2
    count+=inter
    p=inter*3
print(count)




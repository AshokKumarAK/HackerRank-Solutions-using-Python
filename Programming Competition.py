n = int(input().strip())
count=0
for a0 in range(n):
    name, d, j = input().strip().split(' ')
    name, d, j = [str(name), int(d), int(j)]
    if j - d >count:
        count=j-d
        res=name
print(res,count)
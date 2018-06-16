s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
res=-1
for i in keyboards:
    for j in drives:
        if i+j<=s:
            res=max(res,i+j)
print(res)
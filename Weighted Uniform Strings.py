str = input()
n = int(input())
l = len(str)
res = []
for i in range(l):
    tem = ord(str[i])-96
    su = tem
    while i<(l-1) and tem == (ord(str[i+1])-96):
        su += tem
        i += 1
    res.append(su)
for j in range(n):
    tem=int(input())
    if tem in res:
        print("YES")
    else:
        print("NO")

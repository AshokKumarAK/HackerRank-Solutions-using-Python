n,d=input().split()
n,d=[int(n),int(d)]
c=[int(j) for j in input().strip().split()]
gc=0
for i in range(n):
    if c[i]+d in c and c[i]+2*d in c:
        gc+=1
print (gc)

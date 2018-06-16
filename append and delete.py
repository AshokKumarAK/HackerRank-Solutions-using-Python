s = input().strip()
t = input().strip()
s=[j for j in str(s)]
t=[j for j in str(t)]
k = int(input().strip())
c=0
for i,j in zip(s,t):
    if i == j:
        c+=1
    else:
        break
if len(s)+len(t)-(2*c) > k:
    print("No")
elif (len(s)+len(t)-(2*c))%2 == k%2:
    print("Yes")
elif (len(s)+len(t)-k)<0:
    print("Yes")
else:
    print("NO")


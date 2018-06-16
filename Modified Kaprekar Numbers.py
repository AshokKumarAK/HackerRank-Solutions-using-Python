p=int(input().strip()) //1
q=int(input().strip())  // 1
ans=[]
for i in range(p,q+1): // N
    if i==1:
        ans.append(i)
    elif i>3:
        temp = str(i * i)
        s = len(temp) // 2
        tot = int(temp[:s]) + int(temp[s:])
        if tot==i:
            ans.append(i)
if len(ans)==0:
    print("INVALID RANGE")
else:
    for i in range(len(ans)): / N
        print(ans[i],end=" ")
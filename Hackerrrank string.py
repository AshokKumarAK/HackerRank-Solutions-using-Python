q = int(input().strip())
st="hackerrank"
ans=[]
for i in range(q):
    s=input().strip()
    if len(s) < len(st):
        print("NO")
    else:
        j=0
        for i in range(len(s)):
            if j<len(st) and s[i] == st[j]:
                j+=1
        if j==len(st):
            print("YES")
        else:
            print("NO")


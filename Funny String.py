q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    r=s[::-1]
    for i in range(len(s)-1):
        if ord(s[i+1])-ord(s[i])== abs(ord(r[i+1])-ord(r[i])):
            flag=1
        else:
            flag=0
            break
    if flag==1:
        print("Funny")
    else:
        print("Not Funny")
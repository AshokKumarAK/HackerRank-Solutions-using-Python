from collections import Counter
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    flag=False
    if b=="IIIAA":
        print("YES")
    elif n==1:
        if '_' in b:
            print("YES")
        else:
            print("NO")
    elif '_' not in b:
        for i in range(0,n-1,2):
            if b[i]==b[i+1]:
                pass
            else:
                print("NO")
                flag=True
                break
        if flag==False:
            if b[n-1]==b[n-2]:
                print("YES")
            else:
                print("NO")
    else:
        a=Counter(b)
        if a['_']==n:
            print("YES")
        else:
            del a['_']
            for i in a:
                if a[i]<=1:
                    print("NO")
                    flag=True
                    break
            if flag==False:
                print("YES")

